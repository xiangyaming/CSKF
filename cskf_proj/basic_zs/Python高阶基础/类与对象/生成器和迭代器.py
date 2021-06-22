# -*- coding:utf-8 -*-
# @FileName  :推导式.py
# @Time      :2021/4/14 0014 21:51
# @Author    :xiaoming
# -----------------------------------------------------

# url=['page1','page2'....'page100']
urls = []
for i in range(1, 101):
    url = 'page{}'.format(i)
    urls.append(url)
print(urls)

# 列表推导式
urls1 = ['page{}'.format(i) for i in range(1, 101)]
print(urls1)

# 字典推导式
dic = {'name%s' % (i,): i + 1 for i in range(1, 101)}
print(dic)

# () 生成器表达式
t = (i for i in range(10))    #-->生成器对象
a=next(t)                     # next(),用一个，取一个，按顺序取
print(t)

# 通过yield 定义生成器

def func():
    yield
    print('..........')

# 可迭代对象，可以通过for循环遍历   内部只定义了 --iter--方法
li = [1, 2, 3]
b = iter(li)   # -->迭代器，li就是一个可迭代对象
# 迭代器，内部实现了--iter--方法，还实现了--next--方法，可通过next()取值
print(next(b))

# 迭代器与生产器的区别，生产器多了几个方法，send():发送数据，close（）：关闭生成器，throw（）
# 生成器是迭代器的一种

m=([i,j] for i in range(1,5) for j in range(1,5))