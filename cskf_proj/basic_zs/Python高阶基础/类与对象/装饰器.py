# -*- coding:utf-8 -*-
# @FileName  :装饰器.py
# @Time      :2021/4/16 0016 00:34
# @Author    :xiaoming
# -----------------------------------------------------

# 遵循开放封闭原则（面向对象的核心）：对拓展是开放的，对修改是封闭的
# 作用：在不修改源代码的情况下实现对函数的拓展
# 应用场景：
# 1.登录验证
# 2.函数运行时间的统计
# 3.执行函数之前的准备工作
# 4.执行完函数的清理工作

username = 'python'
password = '123456'


def login(func):
    def fun():
        user = input('请输入用户名:')
        pwd = input('请输入密码:')
        if user == username and pwd == password:
            func()
        else:
            print('用户名或者密码错误')
    return fun


@login   # @login:语法糖  --> index = login(index)
def index():
    print('欢迎来到我的首页')


index()

# -------------------------------------
def jisuan(func):
    def fun(a, b):
        print('两数相减：', a - b)
        print('两数相乘：', a * b)
        print('两数相除：', a / b)

        func(a, b)

    return fun


@jisuan
def add(a, b):
    print('两数相加：', a + b)


add(50, 10)


# 通用装饰器（带参数和不带参数都可以）
# def tongyong(func):
#     def fun(*args, **kwargs):
#         print('要装饰的功能代码')
#         func(*args, **kwargs)
#
#     return fun

# --------------------------------------
# 装饰器装饰类
def tongyong(func):
    def fun(*args, **kwargs):
        print('要装饰的功能代码')
        func(*args, **kwargs)
        return func(*args, **kwargs)   # 装饰类的时候一定return，返回func(),才能实例化一个类

    return fun


@tongyong
class MyClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age


print(MyClass('xym', 18))

# -----------------------------------
# Python自带的三个装饰器：@classmethod,@staticmethod,@property
class MyTest:

    @classmethod
    def func1(cls): # cls代表类本身，实例和类都可以调用
        print(cls)
        print('这是一个类方法')

    @staticmethod
    def func2():  # 实例和类都可以调用
        print('这是一个静态方法')

    def func3(self):  # self代表实例本身，只能实例调用
        print('这是一个实例方法')

    @property
    def func4(self):    # 设置只读属性 , 实例.函数名
        print('这个装饰器设定后，该方法可以向熟悉一样调用')
        return '返回值'


obj = MyTest()

obj.func1()
MyTest.func1()
obj.func2()
MyTest.func2()
obj.func3()
print(obj.func4)


