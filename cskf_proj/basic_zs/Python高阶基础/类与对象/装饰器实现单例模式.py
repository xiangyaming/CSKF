# -*- coding:utf-8 -*-
# @FileName  :装饰器实现单例模式.py
# @Time      :2021/4/17 0017 15:30
# @Author    :xiaoming
# -----------------------------------------------------

# 装饰器实现单例模式???


def single(func):
    instance = {}  # instance用来判断是否已经实例化过了

    def fun(*args, **kwargs):
        if func in instance:
            return instance[func]
        else:
            instance[func] = func(*args, **kwargs)
            return instance[func]

    return fun

@single      # -->MyClass=single(MyClass)
class Myclass1:
    pass

obj = Myclass1()        # 创建实例，实际上是执行fun函数