from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator
# from lib.log import log
from web.models import Host, HostType

class HostView(View):
    template_name = 'host.html'
    def get(self, request):
        hosts_list = Host.objects.all()
        paginator = Paginator(hosts_list, 10) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # types = HostType.objects.all()
        # hosttypes = {}
        # for t in types:
            # if t.host_type in hosttype:
                # hosttype[t.host_type].append(t.host_sub_type)
            # else:
                # hosttype[t.host_type] = [t.host_sub_type]
        return render(self.request, self.template_name, {"page_obj": page_obj})

    def post(self, request):

        host = Host(
            host_type = request.POST.get("host_type") or "linux",
            host_name = request.POST['host_name'],
            user_name = request.POST['user_name'],
            host_port = request.POST.get("host_port") or 22,
            host_ip = request.POST['host_ip'],
            # passwd = request.POST['passwd'],
            )
        host.save()
        messages.add_message(request, messages.SUCCESS, 'Save successed.')
        return redirect("/host/")

class HostTypeView(View):
    def post(self, request):
        host_type = request.POST['type']
        host_sub_type = request.POST['sub_type']
        type_id = f"{host_type}@{host_sub_type}"
        hosttype = HostType(host_type=host_type, host_sub_type=host_sub_type, type_id=type_id)
        hosttype.save()
        return JsonResponse({"msg": "successedddd"})
    def get(self, request):
        types = HostType.objects.all()
        return JsonResponse(types)