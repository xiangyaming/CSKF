# -*- coding:utf-8 -*-
# @FileName  :死锁.py
# @Time      :2021/4/19 0019 22:42
# @Author    :xiaoming
# -----------------------------------------------------
import threading
import time

# 死锁

# 创建锁
lock_a = threading.Lock()
lock_b = threading.Lock()

a = 0


def func1():
    global a
    for i in range(1000000):
        # 加锁
        lock_b.acquire()
        lock_a.acquire()
        a += 1
        # 释放锁
        lock_a.release()
        lock_b.release()
    print('线程1修改后的a', a)


def func2():
    global a
    for i in range(1000000):
        # 加锁
        lock_a.acquire()
        lock_b.acquire()
        a += 1
        # 释放锁
        lock_b.acquire()
        lock_a.release()
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


# # 避免死锁，用递归锁
# lock_a = threading.RLock()
# lock_b = threading.RLock()
# a = 0
#
#
# def func1():
#     global a
#     for i in range(1000000):
#         # 加锁
#         lock_b.acquire()
#         lock_a.acquire()
#         a += 1
#         # 释放锁
#         lock_a.release()
#         lock_b.release()
#     print('线程1修改后的a', a)
#
#
# def func2():
#     global a
#     for i in range(1000000):
#         # 加锁
#         lock_a.acquire()
#         lock_b.acquire()
#         a += 1
#         # 释放锁
#         lock_b.acquire()
#         lock_a.release()
#     print('线程2修改后的a', a)
#
#
# s_time = time.time()
# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# e_time = time.time()
# print('最终的a', a)
# print('执行时间：', e_time-s_time)