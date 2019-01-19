# 工作进程
import time
from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManager(BaseManager):
    pass

# 注册获取Queue的方法
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务进程
manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
manager.connect()

# 获取服务进程初始化的Queue对象
task_queue = manager.get_task_queue()
result_queue = manager.get_result_queue()

# 从task_queue取任务，向result_queue里写
for i in range(10):
    try:
        get = task_queue.get(timeout=1)
        print('execute task %s' % get)
        time.sleep(1)
        result_str = "execute task %s success" % get
        result_queue.put(result_str)
    except Queue.Empty:
        print('task queue is empty')
print('worker ended')