from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def home(request):
    return render(request, "index.html")

def cli(request):
    return render(request, "cli.html")

def template(request):
    return render(request, "index.html")


def hosts(request):
    return render(request, "hosts.html")


def tasks(request):
    return render(request, "exec-tasks.html")


@csrf_protect
def add_host(request):
    return render(request, "hosts.html")