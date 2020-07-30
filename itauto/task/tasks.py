# Create your tasks here
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from core.communicate.channel import Channel
from core.ansible.runtask import RunTasks
# from demoapp.models import Widget


@shared_task
def add(x, y):
    return x + y

@shared_task
def send_test(token):
    message = {
                'hostname': 'hostname',
                'port': 'hostname',
                'username': 'hostname',
                'command': 'hostname'
            }
    time.sleep(3)
    Channel.send_msg(token, message)

@shared_task
def ansible_run(data):
    token = data.get("token")
    if token is None:
        return {}
    runner = RunTasks(token=token)
    runner(1, 2, 3)


@shared_task
def xsum(numbers):
    return sum(numbers)