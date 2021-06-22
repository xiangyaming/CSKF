# -*- coding:utf-8 -*-
# @FileName  :队列.py
# @Time      :2021/4/19 0019 23:18
# @Author    :xiaoming
# -----------------------------------------------------

import queue

"""
队列分三种：
1.先入先出队列
2.后入先出队列
3..优先级队列
"""

# 1.先入先出队列
q =queue.Queue(3)  # 可指定添加的数据，最多可添加三条，可修改
# 往队列中添加数据
q.put(1)
q.put(2)
q.put(3)
# q.put(4, block=False)    # 往队列里面添加数据（不等待），如果队列已满，会报错
# q.put_nowait(5)

# 获取队列中的数据
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(block=False))      # 获取数据不等待，如果队列里面获取完了(为空)，会报错
# print(q.get_nowait())

# 获取队列中的任务数
print(q.qsize())

# 判断队列任务是否已满
print(q.full())

# 判断队列是否为空
print(q.empty())

# 判断队列中的任务是否执行完毕
q.task_done()
q.task_done()
q.task_done()
print(q.join())         # 根据q.task_done()来判断是否执行完毕，执行一条，认为完成一条


# 2.后入先出队列
q2 = queue.LifoQueue()
q2.put(1)
q2.put(2)
q2.put(3)
print(q2.get())


# 3..优先级队列
q3 = queue.PriorityQueue()
q3.put((23,'QQ'))        # 插入数据以元组的形式插入
q3.put((111,'QQ'))
q3.put((2,'QQ'))
print(q3.get())
print(q3.get())
