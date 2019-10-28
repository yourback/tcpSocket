import threading, time


def TestA():
    cond.acquire()
    print('李白：看见一个敌人，请求支援')
    cond.wait()
    print('李白：好的')
    cond.notify()
    cond.release()


def TestB():
    time.sleep(2)
    cond.acquire()
    print('亚瑟：等我...')
    cond.notify()
    cond.wait()
    print('亚瑟：我到了，发起冲锋...')


if __name__ == '__main__':
    cond = threading.Condition()
    testA = threading.Thread(target=TestA)
    testB = threading.Thread(target=TestB)
    testA.start()
    testB.start()
    testA.join()
    testB.join()

# 输出
# 李白：看见一个敌人，请求支援
# 亚瑟：等我...
# 李白：好的
# 亚瑟：我到了，发起冲锋...
