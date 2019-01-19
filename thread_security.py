# 多线程安全
# lock = threading.Lock()获取 lock.acquire()获取锁 lock.release()释放锁

import threading,time

lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        # 获取锁:
        lock.acquire()
        try:
            # 避免死锁用try...finally
            pass
        finally:
            # 改完了一定要释放锁:
            lock.release()


# python死循环不能用多线程任务将多核心占满，因为GIL锁的存在：Global Interpreter Lock
# 任何 Python 线程执行前，必须先获得GIL 锁，然后，每执行 100 条字节码，解释器就自动释放 GIL 锁，让别
# 的线程有机会执行
# GIL 全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在 Python 中只能交替执行
# python不能利用多线程实现多核任务，但可以通过多进程实现多核任务


# ThreadLocal 不同线程获取其对应的
# ThreadLocal 最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息
th_local = threading.local()


def pro_thread():
    stu = th_local.student
    print(stu, 'in', threading.current_thread().name)


# 将当前线程与对象绑定
def binding_local(name):
    th_local.student = name
    time.sleep(1)
    pro_thread()


t1 = threading.Thread(target=binding_local, args=('Alice',), name='Thread-3')
t2 = threading.Thread(target=binding_local, args=('Bob',), name='Thread-2')

print('-------------------')
t1.start()
t2.start()
t1.join()
t2.join()
