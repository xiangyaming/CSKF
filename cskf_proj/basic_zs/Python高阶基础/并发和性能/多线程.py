# -*- coding:utf-8 -*-
# @FileName  :多线程.py
# @Time      :2021/4/19 0019 01:39
# @Author    :xiaoming
# -----------------------------------------------------

# 线程：程序运行的最小单位，是一堆指令集。--多线程共享内存空间
# 进程：包含一个或者多个线程，彼此之间是独立的，程序的实例。 --进程内共享数据，进程间不能直接通信

# GIL 全局解释权锁，同一时刻，只能有一个线程进入到解释器，所以Python不能并行，只能并发，CPU快速的切换

# io密集型，多线程运行快
# CPU密集型，单线程块，Python3.7后做了优化，时间差不多了


import time
import threading


def func1():
    for i in range(10):
        print('线程1的执行结果：%s' % (i,))
        time.sleep(1)

def func2():
    for i in range(6):
        print('线程2的执行结果：%s' % (i,))
        time.sleep(1)


obj1 = threading.Thread(target=func1)   # target=传入的目标对象, args=()，对象要传的参数放在args里面
obj2 = threading.Thread(target=func2)

start_time = time.time()
# 设置守护线程。
"""
--放在start之前
1.如果主线程报错了，子线程直接结束. 
2.如果主线程执行完，就不等守护线程执行完，直接结束
"""
obj1.setDaemon(True)
obj1.start()
obj2.start()
# obj1.join()  # join() 等待子线程结束后，主线程才开始执行
obj2.join()
end_time = time.time()
print('运行时间：', start_time-end_time)





