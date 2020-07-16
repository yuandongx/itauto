from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task
from django.core.paginator import Paginator
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