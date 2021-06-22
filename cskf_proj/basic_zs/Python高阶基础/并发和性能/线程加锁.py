# -*- coding:utf-8 -*-
# @FileName  :线程加锁.py
# @Time      :2021/4/19 0019 21:48
# @Author    :xiaoming
# -----------------------------------------------------
import time
import threading

# 线程不安全，多个线程修改同一个全局变量，CPU可能切换到别的线程，造成冲突
# 为解决线程不安全，引入同步机制的互斥锁
# 加锁的时候要避免死锁

# 创建锁
lock = threading.Lock()

a = 0


def func1():
    global a
    for i in range(1000000):
        # 加锁
        lock.acquire()
        a += 1
        # 释放锁
        lock.release()
    print('线程1修改后的a', a)


def func2():
    global a
    for i in range(1000000):
        # 加锁
        lock.acquire()
        a += 1
        # 释放锁
        lock.release()
    print('线程2修改后的a', a)


s_time = time.time()
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.start()
t2.start()
t1.join()
t2.join()
e_time = time.time()
print('最终的a', a)
print('执行时间：', e_time-s_time)






