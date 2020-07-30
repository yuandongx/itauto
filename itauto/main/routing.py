#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:wd

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from core.communicate.routing import websocket_urlpatterns
# from core.consumer.consumers import websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(
        websocket_urlpatterns
    )),
    # 'channel': ChannelNameRouter({
        # 'ssh_exec': TestChannels,
    # }),
})

