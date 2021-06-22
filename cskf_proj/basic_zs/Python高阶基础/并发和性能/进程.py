# -*- coding:utf-8 -*-
# @FileName  :进程.py
# @Time      :2021/4/20 0020 01:40
# @Author    :xiaoming
# -----------------------------------------------------

# 多进程，对CPU密集型的可以使用多进程
# 多进程，不共享全局变量

from multiprocessing import Process
from time import sleep

def work1():
    for i in range(10):
        print('---任务1---')
        sleep(1)

def work2():
    for i in range(10):
        print('---任务2---')
        sleep(1)


if __name__ == '__main__':   # 不加main，下面的代码会在另一个进程导入，陷入无限递归导入

    p1 = Process(target=work1)
    p2 = Process(target=work2)
    p1.start()
    p2.start()