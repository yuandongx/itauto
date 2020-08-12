from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, "index.html")

def cli(request):
    return render(request, "cli.html")

def template(request):
    return render(request, "index.html")


def tasks(request):
    return render(request, "exec-tasks.html")
