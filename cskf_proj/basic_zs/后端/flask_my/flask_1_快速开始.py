# wsgi web Server Gateway Interface
# WSGI是一套接口标准协议/规范；
# 通信（作用）区间是Web服务器和Python Web应用程序之间；
# 目的是制定标准，以保证不同Web服务器可以和不同的Python程序之间相互通信
# 首先，我们明确一下web应用处理请求的具体流程：
# 用户操作操作浏览器发送请求；
# 请求转发至对应的web服务器
# web服务器将请求转交给web应用程序，web应用程序处理请求
# web应用将请求结果返回给web服务器，由web服务器返回用户响应结果
# 浏览器收到响应，向用户展示
# 可以看到，请求时Web服务器需要和web应用程序进行通信，但是web服务器有很多种啊，Python web应用开发框架也对应多种啊，
# 所以WSGI应运而生，定义了一套通信标准。试想一下，如果不统一标准的话，就会存在Web框架和Web服务器数据无法匹配的情况，那么开发就会受到限制，这显然不合理的。#
# 既然定义了标准，那么WSGI的标准或规范是？#
# web服务器在将请求转交给web应用程序之前，需要先将http报文转换为WSGI规定的格式。
# # WSGI规定，Web程序必须有一个可调用对象，且该可调用对象接收两个参数，返回一个可迭代对象：#
# environ：字典，包含请求的所有信息
# start_response：在可调用对象中调用的函数，用来发起响应，参数包括状态码，headers等

# pip install flask
# werkzeug(处理application) jinjia2(渲染html)
# flask ：组装大师
# ORM,数据库等都要安装第三方插件
# flask ==>关注用法，原理和核心思维
# Django ==》具体使用，快速开发，效率

from flask import Flask, request, render_template

# 初始化application
app = Flask(
    __name__,  # __name__,或者自己加一个app名字
    template_folder="html"
)

app.config['DEBUG'] = True
app.config['port'] = 5002

# 添加路由,视图函数
@app.route('/')
def index():
    # 1.接受参数
    # 2.调用对应的函数去处理数据（model）
    # 3.构建响应结果
    # 返回HTML文件，导入render_template
    return render_template('index.html')


@app.route('/login')
# 其他装饰器函数要放在 @app.route下面
# 装饰器的返回值必须是视图函数的返回值
def login():
    return '登录成功'


if __name__ == '__main__':
    # 运行服务器:run()是Python自带的，用来调试，自测，开发。  生成环境用uwsgi,nginx等专门的web服务器
    app.run(debug=app.config['DEBUG'], port=app.config['port'])
    # debug=True,1.修改代码后会重新启动服务，2.出错的时候可以在前端显示错误信息，3.命令行方式运行

    # mvc分层设计  ==>model层， view层（HTML）， control(视图函数)
