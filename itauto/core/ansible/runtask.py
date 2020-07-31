#!/usr/bin/env python

import json
import shutil
from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible import context
import ansible.constants as C
from core.ansible.callback.result import ResultCallback
try:
    from core.communicate.channel import Channel
    HAS_CHANNEL = True
except ImportError:
    HAS_CHANNEL = False
class RunTasks():
    def __init__(self, *args, **kwargs):
        # since the API is constructed for CLI it expects certain options to always be set in the context object
        context.CLIARGS = ImmutableDict(connection=kwargs.get("connection") or 'local',
                                        module_path=kwargs.get("module_path") or [],
                                        forks=10,
                                        become=kwargs.get("become", False),
                                        become_method=kwargs.get("become_method"),
                                        become_user=kwargs.get("become_user"),
                                        check=kwargs.get("check") or False,
                                        diff=kwargs.get("diff")) or False

        # initialize needed objects

        self._loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
        self._passwords = dict(vault_pass='secret')

        # Instantiate our ResultCallback for handling results as they come in. Ansible expects this to be one of its main display outlets
        self._token = kwargs.get("token")
        self._callback = ResultCallback(token=self._token, socket_path=kwargs.get("socket_path"))

        # create inventory, use path to host config file as source or hosts in a comma separated string
        self._inventory = InventoryManager(loader=self._loader, sources='localhost,')

        # variable manager takes care of merging all the different sources to give you a unified view of variables available in each context
        self._variable_manager = VariableManager(loader=self._loader, inventory=self._inventory)
    def __call__(self, name, hosts, tasks, gather_facts="no"):
        # create data structure that represents our play, including tasks, this is basically what our YAML loader does internally.
        play_source =  dict(
                name = "Ansible Play",
                hosts = 'localhost',
                gather_facts = 'no',
                tasks = [
                    dict(action=dict(module='shell', args='ls'), register='shell_out'),
                    dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
                 ]
            )
        # Create play object, playbook objects use .load instead of init or new methods,
        # this will also automatically create the task objects from the info provided in play_source
        play = Play().load(play_source, variable_manager=self._variable_manager, loader=self._loader)

        # Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
        tqm = None
        try:
            tqm = TaskQueueManager(
                      inventory=self._inventory,
                      variable_manager=self._variable_manager,
                      loader=self._loader,
                      passwords=self._passwords,
                      stdout_callback=self._callback,  # Use our custom callback instead of the ``default`` callback plugin, which prints to stdout
                  )
            result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
            print("ansible", result)
        finally:
            # we always need to cleanup child procs and the structures we use to communicate with them
            if tqm is not None:
                tqm.cleanup()
            if HAS_CHANNEL:
                Channel.send_msg(self._token, "tasks finished!")
            # Remove ansible tmpdir
            shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)