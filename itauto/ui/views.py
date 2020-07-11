from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.md")

def cli(request):
    return render(request, "index.md")

def template(request):
    return render(request, "index.md")

def tasks(request):
    return render(request, "index.md")