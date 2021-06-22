# -*- coding:utf-8 -*-
# @FileName  :魔术方法.py
# @Time      :2021/4/17 0017 01:41
# @Author    :xiaoming
# -----------------------------------------------------

# 魔术方法： __xx__() ，__init__之前会执行__new__

class MyClass(object):
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('这是一个new方法')
        # return super().__new__(cls)   # 重写父类的new方法，必须返回父类的new方法，不然无法初始化
        return object.__new__(cls)

obj = MyClass('XYM')
print(obj.name)


# 单例模式，只创建一个实例。每次创建实例，始终返回第一次创建的实例
class OneInstance:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

obj1 = OneInstance()
obj1.name = 'xym'

obj2 = OneInstance()
print(obj2.name)  # pycharm无法识别是一个单利模式



# __str__(),__repr__()
class MyClass(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print('str方法')
        return self.name  # 给用户看，直观

    def __repr__(self):
        print('repr方法')
        return '<MyClass.object-%s>' % (self.name,)  # 一般给IT调试用

    def __call__(self, *args, **kwargs):
        print('我是call方法')


o = MyClass('huahua')
# print,str,format都会执行__str__方法，找不到就会执行__repr__(),都没有就会去父类object里面找
print(o)
print(str(o))
print(format(o))
repr(o)

# __call__()   函数为什么能用函数（）调用，是因为实现了__call__()
o()  # -->我是call方法


# 通过类来实现装饰器????
class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("装饰器里面的功能")
        self.func()


@Decorator
def test():
    print('test代码')


test()

# __new__: 实例化对象的时候调用。 __str__: print(),str(),repr()的时候触发。 __call__:类对象执行的时候触发 -->类（）（）

# __dict__,查看类里面的属性 print(类.__dict__)，每创建一个类，就生成一个__dict__,每创建一个对象就存在__dict__ 里面
# __slots__ = ['name', 'age"], 用来限制类的属性，节约内存，定义了__slots__后，不会再生成__dict__属性
