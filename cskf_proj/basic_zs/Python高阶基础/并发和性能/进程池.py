# -*- coding:utf-8 -*-
# @FileName  :进程池.py
# @Time      :2021/4/21 0021 21:32
# @Author    :xiaoming
# -----------------------------------------------------

from multiprocessing import Pool, Manager,Queue  # pool里面的队列和进程里的不一样
import os, time
import requests


a = 0


def work(q):
    global a
    url = q.get()
    requests.get(url)
    print('work正在执行任务----%s' % (os.getpid()))
    a += 1

if __name__ == '__main__':
    # 进程池中的队列
    q = Manager().Queue()

    for i in range(10):
        q.put('http://www.baidu.com')

    # 创建三个进程池（3个进程）
    pool = Pool(3)
    while 1:
        if q.qsize() > 0:
            pool.apply_async(func=work,args=(q,))
        else:
            break

    pool.close()        # 关闭进程池，关闭后不再接受新的请求
    pool.join()         # 等待pool中所有进程执行完毕，必须放在close语句之后


# 线程也有线程池

# 线程的队列（只能在一个进程中使用）：queue.Queue()
# 进程间的通信（可以在多个进程中使用）： Queue()
# 进程池的队列（给进程池中的队列使用）： Manager().Queue()

