# -*- coding:utf-8 -*-
# @FileName  :多线程_类的方式创建.py
# @Time      :2021/4/19 0019 20:51
# @Author    :xiaoming
# -----------------------------------------------------

import threading
import requests
import time


class RequestThread(threading.Thread):
    """发送request请求的线程类"""

    # 自己定义线程就要继承__init__方法
    def __init__(self, url):
        self.url =url
        super().__init__()

    def run(self):
        res = requests.get(self.url)
        print('线程：{}--返回的状态码：{}'.format(threading.current_thread(), res.status_code))


s_time = time.time()
# 创建5个线程
for i in range(5):
    thread = RequestThread('https://www.163.com/')
    thread.start()

thread.join()
e_time = time.time()
print('耗时： ', e_time-s_time)