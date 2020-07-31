#!/usr/bin/env python
import socket
import struct
import uuid
import os
from threading import Thread
from .utils import to_bytes, to_text
from core.log import log
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
layer = get_channel_layer()


def send_data(s, data):
    packed_len = struct.pack('!Q', len(data))
    return s.sendall(packed_len + data)


def recv_data(s):
    header_len = 8  # size of a packed unsigned long long
    data = to_bytes("")
    while len(data) < header_len:
        d = s.recv(header_len - len(data))
        if not d:
            return None
        data += d
    data_len = struct.unpack('!Q', data[:header_len])[0]
    data = data[header_len:]
    while len(data) < data_len:
        d = s.recv(data_len - len(data))
        if not d:
            return None
        data += d
    return data



def client_send(sock_path, data):

    if data is None:
        return
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sf:
        sf.connect(sock_path)
        send_data(sf, to_bytes(data))


def runserver(channel_name):
    lserver = LocalServer(channel_name)
    th = Thread(target=lserver.run, args=())
    th.start()
    return lserver


class LocalServer(object):
    def __init__(self, channel_name):
        self.signal_stop = False
        self.socket_path = "/tmp/it-auto.%s.tmp" % uuid.uuid4()
        self.channel_name = channel_name
    def run(self):
        try:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            s.bind(self.socket_path)
            s.listen(1)
            # with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
            while self.signal_stop is False:
                (conn, addr) = s.accept()
                with conn:
                    data = recv_data(conn)
                    self.hannder(data)
        except Exception as e:
            print(e)
        finally:
            if os.path.exists(self.socket_path):
                os.remove(self.socket_path)
    def stop(self):
        self.signal_stop = True
        os.remove(self.socket_path)
    def hannder(self, data):
        message = {
                'type': 'ansible.web',
                'message': to_text(data),
            }
        log.debug("hannder[local]"+ str(message))
        log.debug("channel_name[local]" + self.channel_name)
        async_to_sync(layer.group_send)(self.channel_name, message)
    def connect_timeout(self, signum, frame):
        msg = "onnection idle timeout triggered, timeout value is 5s"
        raise Exception(msg)

