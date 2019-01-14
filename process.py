# multiprocessing 模块就是跨平台版本的多进程模块,因为fork只能在Linux/Unix/mac上使用
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process 实例，用 start()方法启动，
# join()方法可以等待子进程结束后再继续往下运行
from multiprocessing import Process
import os


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('--------------------------')
    print('Parent process %s.' % os.getpid())
    # 指定进程需要执行的目标函数和参数列表
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()  # 这句保证了子进程p执行完指定函数后，主进程才继续从之后位置执行
    print('Child process end.')

# 进程池
# 调用 join()之前必须先调用 close()，调用 close()之后就不能继续添加新的 Process
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    # 单位是second
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 不指定进程数量，默认为电脑cpu核数
    p = Pool(2)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # pool在关闭之后无法再加入新的子进程
    p.close()
    # 主进程需要在进程池中所有子进程执行完毕后才继续执行
    p.join()
    print('All subprocesses done.')

# 控制子进程的输入输出
# import subprocess
#
# print('$ nslookup www.python.org')
# # Run command with arguments与命令行调用一致
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# 进程间通信
# 在父进程中创建两个子进程，一个往 Queue 里写数据，一个从 Queue 里读数据
from multiprocessing import Process, Queue
import os, time, random


def p_write(q):
    print('Process to write: %s' % os.getpid())
    for x in ['A', 'B', 'C']:
        print('input %s to queue...' % x)
        q.put(x)
        time.sleep(random.random())


def p_read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=p_write, args=(q,))
    pr = Process(target=p_read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
