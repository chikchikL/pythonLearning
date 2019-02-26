# 主要理解协程的用法
# yield是暂停/开始信号，有yield的函数就是generator，代码运行到yield暂停
# next() 遇到yield表达式暂停，返回yield中的值，再次调用next（）时，从之后的代码开始运行
# send(msg)方法，将当前搁置的yield表达式变为msg，执行之后代码直到下一个yield暂停，第一次调用为send(None)


# 利用协程实现消费者生产者模式
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] consuming %s' % n)
        r = '200 ok'


def producer(c):
    # 初始化generator
    print(c.send(None))
    n = 0
    while n < 5:
        n = n + 1
        print('[Producer] producing %s' % n)
        # send方法的返回值应该是当前yield表达式的值
        result = c.send(n)
        print('[Producer] consumer return %s' % result)
    c.close()


c = consumer()
producer(c)