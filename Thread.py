# threading 是高级模块，对_thread 进行了封装
import threading
import time


# 指定给子线程执行的函数
def th_loop():
    print('%s is running...' % threading.current_thread().name)
    for x in range(5):
        print("%s >>> %s" % (threading.current_thread().name, x))
        time.sleep(1)
    print('%s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    print('%s is running...' % threading.current_thread().name)
    thread = threading.Thread(target=th_loop, name='loop_thread')
    thread.start()
    thread.join()
    print('%s ended.' % threading.current_thread().name)


