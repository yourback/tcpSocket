from pynput import keyboard

from ctypesdemo import OrderAnalysis
from server import SendOrderManager


class KeyListener:

    def __init__(self, socket, order_analysis, event):
        self.event = event
        keyboard_press_listener = keyboard.Listener(on_press=self.on_key_press)
        keyboard_release_listener = keyboard.Listener(on_release=self.on_key_release)
        self.lst = [keyboard_press_listener, keyboard_release_listener]
        self.socket = socket
        self.order_analysis = order_analysis

    def get_listeners(self):
        return self.lst

    def on_key_press(self, key):

        order = ""
        if key == keyboard.Key.up:
            # print('up')
            if self.event.isSet():
                self.event.clear()
            order = self.order_analysis.send_order(SendOrderManager.ORDER_GO_AHEAD)
        elif key == keyboard.Key.down:
            # print('down')
            if self.event.isSet():
                self.event.clear()
            order = self.order_analysis.send_order(SendOrderManager.ORDER_GO_BACK)
        elif key == keyboard.Key.left:
            # print('left')
            if self.event.isSet():
                self.event.clear()
            order = self.order_analysis.send_order(SendOrderManager.ORDER_GO_LEFT)
        elif key == keyboard.Key.right:
            # print('right')
            if self.event.isSet():
                self.event.clear()
            order = self.order_analysis.send_order(SendOrderManager.ORDER_GO_RIGHT)
        elif key == keyboard.Key.home:
            # print("home")
            order = self.order_analysis.send_order(SendOrderManager.ORDER_CUSTOMIZE_1)
        elif key == keyboard.Key.end:
            # print("end")
            order = self.order_analysis.send_order(SendOrderManager.ORDER_CUSTOMIZE_2)
        elif key == keyboard.Key.page_up:
            # print("page_up")
            order = self.order_analysis.send_order(SendOrderManager.ORDER_CUSTOMIZE_3)
        elif key == keyboard.Key.page_down:
            # print("page_down")
            order = self.order_analysis.send_order(SendOrderManager.ORDER_CUSTOMIZE_4)
        elif key == keyboard.Key.space:
            if self.event.isSet():
                self.event.clear()
            order = self.order_analysis.send_order(SendOrderManager.ORDER_MOVE_FREE)
            # print("space")
        if order:
            self.socket.request.sendall(order)

    def on_key_release(self, key):
        if key in [keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right, keyboard.Key.home,
                   keyboard.Key.space]:
            self.event.set()
            self.socket.request.sendall(self.order_analysis.send_order(SendOrderManager.ORDER_STOP))
