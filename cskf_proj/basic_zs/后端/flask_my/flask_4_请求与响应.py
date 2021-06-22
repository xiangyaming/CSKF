# 请求与响应

# OPTIONS : (自带)—>简化版的get，用于询问服务器接口信息。（询问接口支持哪些请求方式，允许哪些请求通过）
# HEAD : （自带）—>简化版的GET请求。只返回GET请求处理的响应头，不返回响应体。（包括状态码）

# URL路径参数
# 转换器语法: <name>
#
# 内置转换器

from flask import Flask
from werkzeug.routing import BaseConverter, UnicodeConverter, AnyConverter, PathConverter, IntegerConverter, FloatConverter, UUIDConverter

app = Flask(__name__)

@app.route('/user/<user_id>')
def get_user_data(user_id):
    return 'get user data {}'.format(user_id)

# note:
# 转换器默认为str类型。
# 指定转换类型<类型名 ：参数名>
# Flask内置的转换器类型：


DEFAULT_CONVERTERS = {
        'default': UnicodeConverter,
        'string': UnicodeConverter,
        'any': AnyConverter,
        'path': PathConverter,
        'int': IntegerConverter,
        'float': FloatConverter,
        'uuid': UUIDConverter,
}

# 2. 自定义转换器
# 创建转换器类，定义匹配正则。



class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'

# note: regex固定
# 2. 将自定义的转换器告知Flask应用

app.url_map.converters['mobile'] = MobileConverter

# 使用自定义转换器
@app.route('/user/<mobile:mob_num>')
def  send_sms_code(mob_num):
    return 'send sms code to {}'.format(mob_num)

# 2. 其它参数
# 通过Flask的request对象获取。

# data: body部分的原始数据。file/form/json/xml…---->bytes类型的字符串。
# from ：表单
# args: 查询字符串（url: /user/1/?a=1 ）中的a = 1
# cookies :
# headers : 请求报文头（一个字典dajngo中字段名大写，flask中字段名小写）
# method ： 请求方法
# url
# files:
# eg:

from flask import request

@ app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')
    return 'you wanna get articles of channel {}'.format(channel_id)


# 往服务器上传文件
from flask import request

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['pic']
    # with open('./demo.png', 'wb') as new_file:
    #     new_file.write(f.read())
    f.save('./demo.png')
    return 'ok'

# 处理响应
# **需求：**在不同的场景里返回不同的响应信息
#
# 1. 返回模板——render_template
# render_template
#
# 在template目录中创建模板文件
# 在视图韩式中返回模板文件
from flask import Flask
from flask import render_template

app = Flask(
__name__)

@app.route('/')
def index():
    mint = 123
    mstr = 'python'
    return render_template('index.html',my_int=mint, my_str=mstr)

# 字典类型数据
# data = {
#     'my_str': 'python',
#     'ny_int': 123
# }
# return render_template('index.html',**data)

# note: django返回的是一个数据字典。

# 重定向——redirect
from flask import redirect

@app.route('/demo2')
def demo2():
    return redirect('http://www.baidu.com')

# 返回json——jsonify
# return json.dumps() # 仅仅是将数据格式转变了。对应的http响应头没有描述信息。Content-Type : application/xml…

# return jsonify

# 转换成了json格式字符串
# 设置了响应头Content-Type :application/json
# content-type:指明了body数据类型。

from flask import jsonify

@app.route('/demo3')
def demo3():
    json_dict = {
		        "user_id" : 10,
		        "user_name": "xyx"
	        }
    return jsonify(json_dict)


# 自定义状态码和响应头
# 1. 元组方式
# 实质：

def func():
    return ret1,ret2,ret3 # ==return (ret1,ret2,ret3)没有一种语言的函数提供返回多值。

ret = func()
ret1,ret2,ret3 = func()

# （响应体body，状态码，响应头）顺序不能变，可省略：1. （响应体）2.（响应体，状态码）3.（响应体，状态码，响应头）
# 响应头传递方式：[（"",""）]、{key:value}
@app.route('/static')
def static():
    return 'response内容', '状态码', '{headers_key:headers_value}'

# 2. make_response方式
@app.route('/static')
def static():
    resp = make_response('make response测试')
    resp.headers['headers_key'] = 'headers_value'
    resp.status = '404 not found'  # 传递完整状态码，状态码+描述信息。
    return resp


# Cookie 与 Session
# Cookie
# 设置 set_cookie 实质：在响应头中增加了一个set_cookie响应头。
# 读取 request.cookies.get 。请求体里有了一个cookies。
# 删除 response.delete_cookie() 实设置过期时间max_age=1970年（响应报文中没有delete相关信息）
# Set-Cookie: name=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/
#
# 设置：response

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/cookie')
def set_cookie():
    resp = make_response('set cookie ')
    resp.set_cookie('username','zhangsan',max_age=10)
    return resp


# 读取：request

from flask import request

@app.route('/request')
def get_request():
    resp = request.cookies.get('username')
    return resp


# 删除：response

@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('delete cookie ok')
    response.delete_cookie()


# Session
# falsk提供了session对象
# 设置：session[name]=value
# 读取：session.get('name)
#
# **note:**直接设置session是会报错的！！！
# must:先设置SECRET_KEY

class DefaultConfig(object):
    SECRET_KEY ='fid8f28jjffldffdao2'

#加载配置参数
app.config.from_object(DefaultConfig)

# or直接设置
app.secret_key = 'fid8f28jjffldffdao2'


# 问题：
#
# session存在哪？
# django默认把session存在本地localsession，或者数据库表里。
# flask: 默认存在浏览器：Cookies目录下有个Session。
# 为什么离不开secret_key?
# 因为flask浏览器session将session保存在浏览器中，别人可随意获取、修改，很不安全。为了增加安全性使用secret_key签名。
# 异常处理

from flask import abort
# if 某种错误:
#     abort(对应状态码)


# 400：bad http request
# 500: 服务器错误
# 404：请求资源找不到
# …

# 异常捕获
# 通用异常：在一个地方集中处理异常
# 代码运行时产生异常：服务器先看该异常有没有申明过，如果申明过则按申明的处理方式返回异常，否则按默认方式抛出异常。
#
# 自己申明错误处理程序
# errorhandler装饰器
# 当程序抛出指定错误的状态码时，就会调用该装饰器所装饰的方法。

@app.errorhandler(400)
def request_error(e):
    return '请求方式错误'


# 如果出现的不是错误状态码，而是异常类
@app.reeorhandler(ZeroDivisionError)
def zero_division_error(e):
    return '除数不能为0'


# e: 所接收到的异常对象。
# 请求钩子
# 实质：中间件的作用，在客户端和服务器的交互过程中有些准备工作和扫尾工作需要处理。
#
# 在请求开始时，建立数据库连接。
# 在请求开始时加你修改一些权限的校验
# 在请求结束时，指定数据的交互格式
# middleware1---->Class Middleware1
# 					def pre_process
# 					def after_process(response)
# 					....
# 					retuen resp
# middleware2
# middleware3
#
#
# 请求的处理过程：pre_process–>view—>after_process
# 中间层提供：pre_process/after_process
#
# 请求钩子，通过装饰器的形式实现，Flask提供了以下四种请求钩子：
#
# before_first_request
# flask启动之后，接到的一个客人。 第一次请求执行前执行
# before_request
# 每一次请求执行前执行
# after_request(response)
# view视图没有出现异常才会执行
# teardown_request(response)
# 每次请求执行后必然执行
# **使用：**在钩子处挂上代码就行。装饰器+函数

@app.before_first_request
def before_first_request():
    print(before_first_request)

# 上下文（2类4种）
# 当不同用户向flask发送request请求时，request作为全局变量，当不同用户用request.args.get(‘user’)能得到各自正确的信息吗？？？
# 概念： 语境、语义
# 1. 请求上下文
# 范围：一个请求之间拿到的数据是一样的。
# request: 封装了HTTP请求的内容，针对的是http请求。举例：user = request.args.get(‘user’)，获取的是get请求的参数。
# session: 用来记录请求会话中的信息，针对的是用户信息。举例：session[‘name’] = user.id，可以记录用户信息。还可以通过session.get(‘name’)获取用户信息。
#
# 2. 应用上下文
# 范围：一个应用之间拿到的数据是一样的。
# current_app：
# 应用程序上下文,用于存储应用程序中的变量，可以通过current_app.name打印当前app的名称，也可以在current_app中存储一些变量，不管谁在这个应用中拿到的这些数据都是一样的。
# 应用的启动脚本是哪个文件，启动时指定了哪些参数
# 加载了哪些配置文件，导入了哪些配置
# 连了哪个数据库
# 有哪些public的工具类、常量
# 应用跑再哪个机器上，IP多少，内存多大
# 使用场景：

# 当需要在蓝图的视图中使用app.config…
# 主程序又使用了蓝图——循环导入。
# 此时可导入：current_app当app使。
# 在主程序中为app添加属性
# 在一个flask工程中创建多个flask应用。current_app==当前运行的应用。
app.redis_cli = 'redis cilent'

# 在其它地方需要使用（比如蓝图视图中）

# current_app.redis_cli

# g对象：
# 实质：存放数据的容器
# 场景：当在一个行数中调用另一个函数时，涉及参数的传递。不管有多少参数都用g对象。
# 小结：
#
# 所有视图的需求——钩子
# 部分视图需求——装饰器
# 各视图之间相互调用传参——g对象
# app_context 与 request_context
# note： 上下文在程序运行时有效，但是在debug模式下无效。——error current_app不处于上下文环境中。
# eg:

app.redis_cli = 'redis client'

from flask import current_app
current_app.redis_cli   # 会报错
# 解决办法
with app.app_contex():
    print(current_app.redis_cli)


# 上下文实现原理---->Threadlocal线程局部
# eg：request为全局对象，同时有多个并发请求，当实现某一具体请求时，通过request对象获取的值不会出错。
# /user？user_id=1 --> request.args.get(‘user_id’)–>1 Thread id a
# /user？user_id=2 --> request.args.get(‘user_id’)–>2 Thread id b
# 原因：request的各个属性存的是多个值，每个值对应不同的线程号。
# 假象为每个线程中的局部变量
