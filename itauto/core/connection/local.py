#!/usr/bin/env python
import socket
import struct
import uuid
import os
from threading import Thread
from utils import to_bytes, to_text


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
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sf:
        sf.connect(sock_path)
        send_data(sf, to_bytes(data))


def runserver(hannder=None):
    lserver = LocalServer()
    lserver.hannder = hannder
    th = Thread(target=lserver.run, args=())
    th.start()
    print(lserver.socket_path)
    # lserver.run()
    return lserver


class LocalServer(object):
    def __init__(self):
        self.signal_stop = False
        self.socket_path = "/tmp/it-auto.%s.tmp" % uuid.uuid4()
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
                    print(data)
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
        print(data)
    def connect_timeout(self, signum, frame):
        msg = "onnection idle timeout triggered, timeout value is 5s"
        raise Exception(msg)

def test_hanner(data):
    with open("/home/ubuntu/www/itauto/core/connection/test.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    l = runserver(test_hanner)
    print(l.socket_path)