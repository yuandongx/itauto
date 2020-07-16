from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import models
# Create your views here.


def add_host(request):
    try:
        if request.POST:
            host = models.Hosts(
                host_type = request.POST['host_type'],
                host_name = request.POST['host_name'],
                user_name = request.POST['user_name'],
                host_port = request.POST['host_port'],
                host_ip = request.POST['host_ip'],
                passwd = request.POST['passwd'],
                )
            host.save()
    except KeyError:
        messages.add_message(request, messages.ERROR, 'Save failed.')
    messages.add_message(request, messages.SUCCESS, 'Save successed.')
    return HttpResponseRedirect(reverse('hosts'))