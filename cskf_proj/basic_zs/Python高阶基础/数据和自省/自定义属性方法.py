# -*- coding:utf-8 -*-
# @FileName  :自定义属性方法.py
# @Time      :2021/4/18 0018 13:33
# @Author    :xiaoming
# -----------------------------------------------------

class Test:

    def __getattr__(self, item):
        # 当我们访问属性的时候，如果属性不存在，抛出attrerro后，触发这个方法
        print('这是getattr方法')
        return '固定属性'

    def __getattribute__(self, item):
        # 访问属性的时候，第一时间触发该属性去查找属性
        print('这是getattibute方法')
        return super().__getattribute__(item)   # 返回一个属性，或者抛出异常
        # return 100

    def __setattr__(self, key, value):
        # 给对象设置属性的时候触发
        print('设置属性的时候触发')
        super(Test, self).__setattr__(key, value)

    def __delattr__(self, item):
        # 删除属性的时候触发  del obj.name
        print('触发__delattr__')
        super().__delattr__(item)


obj =Test()
obj.name='xiaoming'
print(obj.name1)
print(obj.name)
