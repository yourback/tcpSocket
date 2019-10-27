from ctypes import *


# print("传递并返回字符串")
# 字符串转化为byte传送  方法一
# val = bytes('qqqqqq',encoding='utf-8')
# 方法二
# str_test = "need_bytes"
# val = str_test.encode()
# func.strTest.restype = c_char_p
# print(func.strTest(val))
class OrderAnalysis(object):

    def __init__(self, file_name):
        # func = CDLL("./add.so")
        self.func = CDLL(file_name)

    def send_order(self, order_code: int):
        self.func.get_order_str.restype = c_char_p
        return_str = self.func.get_order_str(order_code)
        return return_str
