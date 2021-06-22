# -*- coding:utf-8 -*-
# @FileName  :描述器.py
# @Time      :2021/4/18 0018 14:32
# @Author    :xiaoming
# -----------------------------------------------------

class Filed:

    # 一个类中，只要定义了以下三个方法中的任意一个，就是一个描述器类
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass

class Model(object):
    name ='xiaoming'
    attr = Filed()  # -->描述器对象 ：会覆盖类属性的相关操作，访问的是描述器里面的方法

obj = Model()
obj.name = 'huahua'
print(obj.name)