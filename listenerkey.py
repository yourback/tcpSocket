from pynput import keyboard

from ctypesdemo import OrderAnalysis
from send_tool import SendOrderManager


class KeyListener:

    def __init__(self, socket, c_file_name):
        keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.lst = [keyboard_listener]
        self.socket = socket
        self.order_analysis = OrderAnalysis(c_file_name)

    def get_listeners(self):
        return self.lst

    def on_key_press(self, key):
        order = ""
        if key == keyboard.Key.up:
            print('up')
            order = self.order_analysis.send_order(SendOrderManager.ORDER_GO_AHEAD)
        elif key == keyboard.Key.down:
            print('down')
            order = self.order_analysis.send_order(SendOrderManager.ORDER_GO_BACK)
        elif key == keyboard.Key.left:
            print('left')
            order = self.order_analysis.send_order(SendOrderManager.ORDER_GO_LEFT)
        elif key == keyboard.Key.right:
            print('right')
            order = self.order_analysis.send_order(SendOrderManager.ORDER_GO_RIGHT)
        elif key == keyboard.Key.home:
            print("home")
            order = self.order_analysis.send_order(SendOrderManager.ORDER_OPEN)
        elif key == keyboard.Key.end:
            print("end")
            order = self.order_analysis.send_order(SendOrderManager.ORDER_CLOSE)

        if order:
            self.socket.request.sendall(order)
