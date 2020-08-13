from django.shortcuts import render
from .host import HostView, HostTypeView



__all__ = ["HostView", "HostTypeView"]


def default(request):
    return render(request, "base.html")