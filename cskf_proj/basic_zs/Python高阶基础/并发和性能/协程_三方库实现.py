# -*- coding:utf-8 -*-
# @FileName  :协程_三方库实现.py
# @Time      :2021/4/21 0021 23:50
# @Author    :xiaoming
# -----------------------------------------------------

import gevent ,time
from gevent import monkey
"""
协程：gevent
协程存在于线程中，线程默认不会等待协程执行
spwn:开启协程
join：等待协程执行
协程切换的条件：gevent.sleep().耗时等待的时候会切换
线程切换的条件：io阻塞，或者达到时间阈值

gevent的补丁：gevent.monkey.patch_call(),只要有等待就会切换

并发： 首先考虑协程，其次线程，最后进程，一般不用进程

"""

def work1():
    for i in range(10):
        print('--work1--任务%s' % i)
        # gevent.sleep(0.1)
        time.sleep(0.01)



def work2():
    for i in range(10):
        print('--work2--任务%s' % i)
        # gevent.sleep(0.1)
        time.sleep(0.01)


# 创建两个协程
gevent.monkey.patch_all()
g1 = gevent.spawn(work1)
g2 = gevent.spawn(work2)
g1.join()
g2.join()