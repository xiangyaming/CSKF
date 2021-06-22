# -*- coding:utf-8 -*-
# @FileName  :队列和线程应用.py
# @Time      :2021/4/20 0020 00:52
# @Author    :xiaoming
# -----------------------------------------------------

import threading
import queue
import time

q = queue.Queue()


# 创建一个队列来存储商品
# 创建一个专门生产商品的线程类，当商品数小于50的时候开始生产商品,每生产一轮停一秒
# 创建一个专门消费的线程类，当商品数量大于10就开始消费，循环消费，每次消费3个当商品小于10的时候听2秒
# 创建一个线程生产商品，5个线程消费商品


class Product(threading.Thread):
    """生产者"""
    def run(self):
        # 判断商品的数量是否小于50,小于50就生成200个
        count = 0
        while 1:
            if q.qsize() < 50:
                for i in range(200):
                    count += 1
                    goods = '第{}个商品-'.format(count)
                    q.put(goods)
                    print('生产：', goods)
                time.sleep(1)


class Consumer(threading.Thread):
    """消费者"""
    def run(self):
        while 1:
            if q.qsize() > 10:
                for i in range(3):
                    print('消费：{}'.format(q.get()))
                time.sleep(2)


p = Product()
p.start()

for i in range(5):
    c = Consumer()
    c.start()