"""tasks URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    path("", views.show, name="tasks"),
    path("cli", views.cli, name="cli"),
    path("cli/get-hosts", views.cli_hosts, name="cli-hosts"),
    path("cli/exec", views.exec_cli_tasks, name="cli-exec"),
    path("add-task", views.add_task),
]