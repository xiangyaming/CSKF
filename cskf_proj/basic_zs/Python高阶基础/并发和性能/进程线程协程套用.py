# -*- coding:utf-8 -*-
# @FileName  :进程线程协程套用.py
# @Time      :2021/4/22 0022 00:32
# @Author    :xiaoming
# -----------------------------------------------------

"""
10000个请求，使用2个进程，进程中开启3个线程，线程中开启5个协程
#30个协程

"""

import time
from threading import Thread
from multiprocessing import Process, Queue
import gevent
import requests

# 计时装饰器
def count_time(func):
    """计时函数装饰器"""
    def fun(*args, **kwargs):
        print('开始执行')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('结束执行')
        print('总耗时：',end_time-start_time)
    return fun


def green_work(q, gname):
    count = 0
    while not q.empty():
        url = q.get(timeout=0.01)
        requests.get(url)
        gevent.sleep(0.001)
        count += 1
    print('----协程{}执行了{}个任务'.format(gname,count))



def thread_work(q,tname):
    """
    每个线程执行的任务数，在线程中开启5个协程
    """
    g_list = []
    for i in range(5):
        gname = '{}-g-{}'.format(tname, i)
        print('协程创建：',gname)
        g = gevent.spawn(green_work, q, gname)
        g_list.append(g)
    gevent.joinall(g_list)


def process_work(q, pname):
    """
    pname:标识是哪个进程
    q:进程间通信的队列

    """
    thread_list = []
    for i in range(3):
        tname = '{}-th-{}'.format(pname, i)
        print('创建线程：', tname)
        t = Thread(target=thread_work, args=(q, tname))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()


@count_time
def main():
    # 创建10000个请求的队列
    q = Queue()
    for i in range(10000):
        q.put('http://127.0.0.1:5000')
    print('队列创建完成，数量为：', q.qsize())
    # 开启两个进程处理
    pro_list = []
    for i in range(2):
        pname = 'pro-{}'.format(i)
        print('创建进程：', pname)
        p = Process(target=process_work, args=(q, pname))
        p.start()
        pro_list.append(p)
    # 等待子进程执行完毕
    for p in pro_list:
        p.join()

if __name__ == '__main__':
    main()
