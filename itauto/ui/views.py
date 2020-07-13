from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def cli(request):
    return render(request, "index.html")

def template(request):
    return render(request, "index.html")


def hosts(request):
    return render(request, "hosts.html")


def tasks(request):
    return render(request, "exec-tasks.html")