# -*- coding:utf-8 -*-
# @FileName  :函数.py
# @Time      :2021/4/15 0015 00:08
# @Author    :xiaoming
# -----------------------------------------------------

from functools import partial  # 偏函数
from functools import reduce


# 递归函数，函数内部调用自己
# 1.调用自身
# 2.有一个结束条件
# 3.能用递归的都能用循环解决
def func(n):
    if n == 1:
        return 1
    return n * func(n - 1)


print(func(5))


# 纯函数，函数结果，只跟传入的参数有关 --概念
# 内置函数  https://www.runoob.com/python/python-built-in-functions.html
# enumerate() ,eval(),map(), filter(), zip(), reduce(), lambda()

def f(n):
    return n < 10


li = [1, 2, 343, 53, 32, 2, 3, 45, 5, 4, 6]
res = filter(f, li)
# res是一个可迭代对象，转换成列表去使用。 filter会遍历li中的元素，传给函数f
print(list(res))


def m(n):
    return n ** 2


res2 = map(m, li)
# res2是一个可迭代对象，转换成列表去使用。 map会遍历li中的元素，传给函数f
print(list(res2))

res3 = zip([1, 2, 3], [111, 222, 333])
# print(list(res3))
# 可通过dict,快速穿件一个字典，list(迭代器)后,值被迭代取出来了，就没有值了
print(dict(list(res3)))

# 匿名函数
res4 = (lambda x, y: x + y)(1, 2)
print(res4)

# 偏函数
filter(lambda x: x < 5, li)
# 偏函数将（lambda x: x < 5）固定住，只需要传一个参数，适用于参数较多的时候
filter2 = partial(filter, lambda x: x < 5)
res5 = filter2(li)
print(list(res5))


# reduce()  函数会对参数序列中元素进行累积
def add(x, y):  # 两数相加
    return x + y


sum1 = reduce(add, [1, 2, 3, 4, 5])  # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
print(sum1)
print(sum2)
