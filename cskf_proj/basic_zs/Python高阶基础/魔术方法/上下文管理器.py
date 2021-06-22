# -*- coding:utf-8 -*-
# @FileName  :上下文管理器.py
# @Time      :2021/4/18 0018 00:05
# @Author    :xiaoming
# -----------------------------------------------------

with open('test.txt', 'w+', encoding='utf8') as f:
    f.write('学习上下文管理器')

# with 后面跟的是一个上下文管理器对象,处理前先会去执行__enter__(),处理完后会执行__exit__()

# 自己实现一个文件操作的上下文管理器
class MyOpen:

    def __init__(self, file_name, open_method, encoding='utf8'):
        self.file_name = file_name
        self.open_method = open_method
        self.encoding = encoding

    def __enter__(self):
        self.f = open(self.file_name, self.open_method, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with MyOpen('test.txt', 'r') as f:
    t = f.read()
    print(t)


    # 实现一个mysql的上下文管理器
    # class DB:
    #
    #     def __init__(self, data_config):
    #         self.con = pymysql.connect(**data_config)
    #         self.cursor = self.con.cursor()
    #
    #     def __enter__(self):
    #         return self.cursor
    #
    #     def __exit__(self, exc_type, exc_val, exc_tb):
    #         self.cursor.colse()
    #         self.con.close()
    #
    # DB_CONF={}
    # with DB(DB_CONF) as cur:
    #     cur.execute("sql语句")
    #     print(cur.fetchone())