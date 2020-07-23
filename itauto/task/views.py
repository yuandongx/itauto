import json
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task
from host.models import Hosts
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from .models import Task
from host.models import Hosts
from core.consumer.channel import Channel 
# Create your views here.

def add_task(request):
    # if request.POST:
    host = Task(
        host_type = request.POST['host_type'],
        host_name = request.POST['host_name'],
        user_name = request.POST['user_name'],
        host_port = request.POST['host_port'],
        host_ip = request.POST['host_ip'],
        passwd = request.POST['passwd'],
        )

    host.save()
    # messages.add_message(request, messages.ERROR, 'Save failed.')
    messages.add_message(request, messages.SUCCESS, 'Save successed.')
    return HttpResponseRedirect(reverse('tasks'))

def show(request):
    tasks_list = Task.objects.all()
    paginator = Paginator(tasks_list, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "tasks.html", {'page_obj': page_obj})


def cli(request):
    return render(request, "tasks-shell.html")

def cli_hosts(request):
    result = []
    hosts = Hosts.objects.all()
    for host in hosts:
        result.append(
            """<tr>
                  <th scope="row"><input id='{host_id}' name='{host_id}' type='checkbox'/></th>
                  <td>{host_type}</td>
                  <td>{host_name}</td>
                  <td>{host_ip}</td>
                </tr>""".format(host_id=host.host_id,
            host_type=host.host_type,
            host_name=host.host_name,
            host_ip=host.host_ip))
    return HttpResponse("".join(result))


def exec_cli_tasks(request):
    token = Channel.get_token()
    host_ids = request.GET.get("host_ids")
    for host in Hosts.objects.filter(host_id=host_ids):
            # Channel.send_ssh_executor(
                # token=token,
                # hostname=host.hostname,
                # port=host.port,
                # username=host.username,
                # command=form.command
            # )
            Channel.send_channel_msg(token,
                dict(
                hostname=host.hostname,
                port=host.port,
                username=host.username,
                command=form.command))
    return JsonResponse(dict(token=token))