from wsgiref.simple_server import make_server


'''
具备三个功能：
1.定义三个URL，'/' 首页，'/login' 登录，'/projects' 项目
2.对三个URL做出对应的响应
3.如果访问不在三个URL中就报404
'''


def home():
    return 'hello'


def login():
    return 'login'


def project():
    return 'project'

# def app(env,start_response):
#     # env 获取请求相关的数据
#     # 状态码，响应头
#     if env.get('PATH_INFO') == '/':
#         start_response('200 ok', [('content-type', 'text/plain'), ])
#         resp = home()
#         return [resp.encode()]
#     elif env.get('PATH_INFO') == '/login':
#         start_response('200 ok', [('content-type', 'text/plain'), ])
#         resp = login()
#         return [resp.encode()]
#     elif env.get('PATH_INFO') == '/project':
#         start_response('200 ok', [('content-type', 'text/plain'), ])
#         resp = project()
#         return [resp.encode()]
#     else:
#         start_response('404 not found', [('content-type', 'text/plain'), ])
#         return [b'page not found']  # type


'''
如果出现了很多条件分支都是 == ，用字典去封装
'''
# flask用装饰器去实现，更灵活
# 路由，建立URL和函数的对应关系， 集中管理
patterns = {
    '/': home,
    '/login': login,
    '/project': project
}


def app(env, start_response):
    """
    env: 获取请求相关的数据
    start_response: 状态码，响应头
    """

    url = env.get('PATH_INFO')
    if url not in patterns.keys():
        start_response('404 not found', [('content-type', 'text/plain'), ])
        return [b'page not found']
    start_response('200 ok', [('content-type', 'text/plain'), ])
    resp = patterns.get(url)
    return [resp().encode()]


server = make_server('', 6001, app)
server.serve_forever()
