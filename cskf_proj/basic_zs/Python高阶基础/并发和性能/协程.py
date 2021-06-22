# -*- coding:utf-8 -*-
# @FileName  :协程.py
# @Time      :2021/4/21 0021 22:54
# @Author    :xiaoming
# -----------------------------------------------------

import time
"""
生成器
生成器表达式
在函数中使用yield关键字

"""
def work1():
    for i in range(10):
        print('--work1--任务%s' % i)
        time.sleep(0.1)
        yield


def work2():
    for i in range(10):
        print('--work2--任务%s' % i)
        time.sleep(0.1)
        yield

g1 = work1()
g2 = work2()

while 1:
    try:
        next(g1)
        next(g2)
    except StopAsyncIteration:
        break

# 协程：微线程，依赖于线程，本质上是单任务，相比于线程，协程占用资源更少
