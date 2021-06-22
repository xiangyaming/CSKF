# -*- coding:utf-8 -*-
# @FileName  :进程的通讯.py
# @Time      :2021/4/20 0020 01:56
# @Author    :xiaoming
# -----------------------------------------------------

from multiprocessing import Process, Queue
import requests

a = 1


def work1(q):
    while q.qsize() > 0:
        global a
        url = q.get()
        requests.get(url)
        print('work1正在执行任务----%s' % (a,))
        a += 1


def work2(q):
    while q.qsize() > 0:
        global a
        url = q.get()
        requests.get(url)
        print('work2正在执行任务----%s' % (a,))
        a += 1


if __name__ == '__main__':
    q = Queue()
    for i in range(9):
        q.put('http://www.baidu.com')

    p1 = Process(target=work1, args=(q,))
    p2 = Process(target=work2, args=(q,))
    p1.start()
    p2.start()
