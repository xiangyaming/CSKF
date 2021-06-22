# -*- coding:utf-8 -*-
# @FileName  :命名元组.py
# @Time      :2021/4/14 0014 20:28
# @Author    :xiaoming
# -----------------------------------------------------


# 可以用来测性能
import timeit
from collections import namedtuple

timeit.Timer()

def func():
    for i in range(10):
        print(i)


# 函数不加‘’，列表，元组等要加‘’ ，100代表执行的次数,默认执行1000万次
res = timeit.Timer(func).timeit(100)
print(res)

# 元组的性能，大大优于列表
res1 = timeit.timeit('[1,2,3]')
print(res1)
res2 = timeit.timeit('(1,2,3)')
print(res2)

# 命名元组
my_tuple = namedtuple('my_tuple', ['name', 'age', 'gender'])
t = my_tuple('xiaoming', 18, 'nan')
print(t)
print(t.name)
print(type(t))
print(type(my_tuple))  # 元类

# 字典和集合，无序，Python3.7后，字典是有序的，按照添加的顺序
# 利用集合对列表去重， 集合是可变的，可以怎删改，交集，并集等
# 不可变，可hash
li = [1, 2, 3, 4, 4, 4, 5, 5, 6]
print(list(set(li)))

