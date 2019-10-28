import socket
import sys
from threading import Thread
from time import sleep


class SocketClient(object):

    def __init__(self, address, intervals):
        self.addr = address
        self.time = intervals
        self.connect_addr()

    # def send_machine_status(self, socket_client):
    #     # send machine info
    #     print('send_machine_status')
    #     while True:
    #         sleep(1)
    #         print('send_1111')
    #         socket_client.send(b"1111111")

    def connect_addr(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            self.socket = sock
            print('connecting')
            sock.connect(self.addr)
            print('connect success')
            # sock.send(b'111')
            # t_order_send = Thread(target=self.send_machine_status, args=[sock, ])
            t_order_recv = Thread(target=self.order_recv, args=[sock, ])
            # t_order_send.start()
            t_order_recv.start()
            # t_order_send.join()
            t_order_recv.join()

    def order_recv(self, socket_client):
        while True:
            received = socket_client.recv(1024)  # struct.unpack("2B",sock.recv(1024))
            if received:
                # print("received order: {}".format(received))
                if received == b'get_status':
                    self.socket.send(b"machine status:  xxxx xxxx xxxx")
                elif received == b'stop':
                    print("machine stopped")


if __name__ == '__main__':
    addr = "127.0.0.1", 8888
    SocketClient(addr, 1)
