"""main URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from ui import views
urlpatterns = [
    path("hosts/", include("host.urls")),
    path("tasks/", include("task.urls")),
    path("home", views.home, name="home"),
    path("template", views.template, name="template"),
    path("", views.template, name="apps-deploy"),
    path("", views.template, name="schedule"),
    path("", views.template, name="environ"),
    path("", views.template, name="service"),
    path("", views.template, name="apps-config"),
    path("", views.template, name="monitor"),
    path("", views.template, name="log"),
    path("", views.template, name="contacts"),
    path("", views.template, name="contacts-grp"),
    path("", views.template, name="accounts"),
    path("", views.template, name="roles"),
    path("", views.template, name="devices"),
    path('admin/', admin.site.urls),
]
