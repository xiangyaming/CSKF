# 可插拔视图 基于类的视图,主要用于前后端分离的时候


from flask import Flask, request
from flask.views import View, MethodView

app = Flask(__name__)


# class ProjectView(View):
#     def get(self):
#         return 'get'
#
#     def post(self):
#         return 'post'
#
#     # 分配请求
#     def dispatch_request(self):
#         dispatch_pattern = {'GET':self.get, 'POST':self.post}
#         method = request.method
#         return dispatch_pattern.get(method)()
#         # return 'project'

# 方法二
class ProjectView(MethodView):

    def get(self):
        return 'get'

    def post(self):
        return 'post'


app.add_url_rule('/project',
                 view_func=ProjectView.as_view('project'),
                 methods=['GET', 'POST'])
# 装饰器装饰的是视图函数，对view_func重新复制装饰，不在用@符号，装饰器名（视图函数）


if __name__ == '__main__':
    app.run(debug=True)
