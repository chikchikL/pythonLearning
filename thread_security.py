# 多线程安全
# lock = threading.Lock()获取 lock.acquire()获取锁 lock.release()释放锁

import threading

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
# 不能利用多线程实现多核任务，但可以通过多进程实现多核任务
