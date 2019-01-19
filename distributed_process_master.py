# 分布式进程，分为服务进程和任务进程，master分发任务到worker进行处理
# Queue 的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小
# 比如发送一个处理日志文件的任务，就不要发送几百兆的日
# 志文件本身，而是发送日志文件存放的完整路径，由 Worker 进程再去
# 共享的磁盘上读取文件
import random, queue
from multiprocessing.managers import BaseManager

print(random.randint(0, 100))

# 初始化队列
queue_task = queue.Queue()
queue_result = queue.Queue()


# 初始化Manager
class QueueManager(BaseManager):
    pass


def get_task_queue():
    global queue_task
    return queue_task


def get_result_queue():
    global queue_result
    return queue_result





if __name__ == '__main__':
    # 将两个队列注册到网络上
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    # 绑定端口并设置验证码
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue
    manager.start()

    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()

    # 向任务队列添加
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task_queue.put(n)

    # 从result队列读取
    print('get results...')
    for i in range(10):
        # 从队列读取元素需要设置超时时长
        get = result_queue.get(timeout=100)
        print('result---', get)

    # 关闭管理者,管理分发任务的服务进程结束
    manager.shutdown()
    print('master exit')