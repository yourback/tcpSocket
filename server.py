import socketserver
import threading
from time import sleep

# from listenerkey import KeyListener
import listenerkey

c_file_name = "./pycso.so"


class SendOrderManager(object):
    ts = []
    # order:move
    ORDER_GO_AHEAD = 0
    ORDER_GO_BACK = 1
    ORDER_GO_LEFT = 2
    ORDER_GO_RIGHT = 3
    # order:keep get info of machine status or not
    ORDER_OPEN = 4
    ORDER_CLOSE = 5

    def __init__(self, socket):
        # init key listener
        kl = listenerkey.KeyListener(socket, c_file_name)
        # if use the open/close order comment out next two sentences
        # init order info
        # t_order_get_info = threading.Thread(target=self.send_order_gei_info)
        # append thread
        # self.ts.append(t_order_get_info)

        self.ts += kl.get_listeners()

        # t_order_move = threading.Thread(target=self.send_order_move)
        # self.ts.append(t_order_move)

    def start_with(self, t):
        self.ts.append(t)
        for t in self.ts:
            t.start()

        for t in self.ts:
            t.join()

    # def send_order_move(self):
    #     while True:
    #         sleep(1)
    #         print('send order move')

    def send_order_gei_info(self):
        """
        order get info
        :return:
        """
        while True:
            sleep(0.5)
            print('send order get info')


class RobotTestTCPHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def handle(self):
        t_recv = threading.Thread(target=self.recv)
        sm = SendOrderManager(self)
        sm.start_with(t_recv)

    def recv(self):
        while True:
            print('接收信息')
            print(self.request.recv(1024).strip())
            print("{} return:".format(self.client_address[0]))


if __name__ == '__main__':
    HOST, PORT = "127.0.0.1", 8888
    server = socketserver.TCPServer((HOST, PORT), RobotTestTCPHandler)
    print("Server started, waiting for a connection...")
    server.serve_forever()

    # sm = SendManager()
    # sm.start()
