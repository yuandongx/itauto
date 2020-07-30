# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from django.urls import re_path
from .consumers import WbChannels
from django.conf.urls import url
websocket_urlpatterns = [
    # path('ws/task/<str:token>/', ExecConsumer),
    url('ws/cli/(?P<token>\S+)/$', WbChannels),
]
