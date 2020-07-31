# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from core.ansible.runtask import RunTasks
from core.log import log
from core.connection import runserver


def ansible_run(token):

    lserver = runserver(token)
    runner = RunTasks(token=token, socket_path=lserver.socket_path)
    runner(1, 2, 3)

# @shared_task, a example
# def xsum(numbers):
    # return sum(numbers)