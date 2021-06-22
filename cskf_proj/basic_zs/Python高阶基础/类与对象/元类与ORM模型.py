# -*- coding:utf-8 -*-
# @FileName  :元类与ORM模型.py
# @Time      :2021/4/18 0018 17:00
# @Author    :xiaoming
# -----------------------------------------------------

# 类都是Type创造的，所有的类都默认继承object类
# type(object) -> the object's type
# type(name, bases, dict) -> a new type

# 自定义元类，必须继承type,  自定义的元类是可以继承的
# class MyMetaClass(type):
#     """ 让类里面所有属性变成大写 """
#     def __new__(cls, name, bases, attr_dict, *args, **kwargs):
#
#         for k, v in attr_dict.items():
#             attr_dict.pop(k)
#             attr_dict[k.upper()] = v
#
#         # return type.__new__(name, bases, attr_dict)
#         return super().__new__(cls, name, bases, attr_dict)
#
#
# class Test(metaclass=MyMetaClass):
#     name = 'xiaoming'
#
#
# print(type(Test))
# print(Test.__dict__)
# print(Test.name)



class MyMetaClass(type):
    """ 模型类的元类 """
    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, attr_dict)
        else:
            table_name = name.lower()   # 把数据库表名转换为小写
            fields ={}                  # 用来存放模型类字段和数据表的对于关系
            for k, v in list(attr_dict.items()):   # 对字典的引用是动态的，for循环后面跟的是一个可迭代对象，转换成list来操作
                if isinstance(v, BaseFiled):    # 判断属性是否为定义的字段类型
                    fields[k] = v

            attr_dict['table_name'] = table_name
            attr_dict['fields'] = fields
            # return type.__new__(name, bases, attr_dict)
            return super().__new__(cls, name, bases, attr_dict)

# 利用元类实现一个模型类
class BaseFiled(object):
    pass


class CharFiled(BaseFiled):

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


class BaseModel(metaclass=MyMetaClass):
    """ 模型类的基类，用来初始化参数 """
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        # 保存一条数据，生成一条sql语句
        # 获取表明
        table_name = self.table_name
        # 获取字段名称
        fields = self.fields
        # 获取字段的值
        field_dict  = {}
        for field in fields.keys():
            field_dict[field] = getattr(self, field)
        # 生成sql
        sql = 'INSERT INTO {} VALUE{};'.format(table_name, tuple(field_dict.values()))
        print(sql)

class UserModel(BaseModel):
    # 用户模型类
    username = CharFiled(10)
    pwd = CharFiled(20)


obj_xiaoming = UserModel(username='小明', pwd='123456')
print(obj_xiaoming.username)
print(obj_xiaoming.table_name)

obj_xiaoming.save()
