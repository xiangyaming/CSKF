"""
初始化APP核心对象
配置一些插件
"""

from flask import Flask
app = Flask(__name__)

def create_app():
    """初始化"""
    # 初始化数据库
    # 配置文件
    # 自定义的错误处理机制
    # 模板过滤器注册
    # @ app.add_template_filter
    return  app

