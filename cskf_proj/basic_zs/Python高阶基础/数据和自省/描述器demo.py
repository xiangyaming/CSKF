# -*- coding:utf-8 -*-
# @FileName  :描述器demo.py
# @Time      :2021/4/18 0018 15:44
# @Author    :xiaoming
# -----------------------------------------------------

class CharFiled:

    def __init__(self, max_length):
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_length:
                self.value = value
            else:
                raise ValueError('超过最大长度限制：%s' % (self.max_length,))
        else:
            raise TypeError('只能传字符串类型的数据')

    def __delete__(self, instance):
        self.value = None


class UserModel(object):
    # 假设这是一个模型类
    name = CharFiled(5)
    pwd = CharFiled(10)

obj = UserModel()

obj.name = '9999999'
print(obj.name)