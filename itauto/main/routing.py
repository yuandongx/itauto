#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:wd

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from core.consumer import routing, executors

application = ProtocolTypeRouter({
    'channel': ChannelNameRouter({
        'ssh_exec': executors.SSHExecutor,
    }),
    'websocket': URLRouter(
        routing.websocket_urlpatterns
    )
})