from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from core.log import log
from host.models import Hosts, HostType

class HostsView(View):
    template_name = 'hosts.html'
    def get(self, request):
        hosts_list = Hosts.objects.all()
        paginator = Paginator(hosts_list, 10) # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(self.request, self.template_name, {'page_obj': page_obj})

    def post(self, request):
        # if request.POST:
        log.info(str(request.POST));
        host = Hosts(
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
        return HttpResponseRedirect(reverse('hosts'))


class HostTypeView(View):
    def post(self, request):
        # if request.POST:
        log.info(str(request.POST));
        host_type = request.POST['type']
        host_sub_type = request.POST['sub_type']
        type_id = f"{host_type}@{host_sub_type}"
        hosttype = HostType(host_type=host_type, host_sub_type=host_sub_type, type_id=type_id)
        hosttype.save()
        # messages.add_message(request, messages.ERROR, 'Save failed.')
        messages.add_message(request, messages.SUCCESS, 'Save successed.')
        return JsonResponse({"save": "successed"})
    def get(self, request):
        types = HostType.objects.all()
        return JsonResponse(types)

