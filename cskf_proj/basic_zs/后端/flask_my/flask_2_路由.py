# 一.url
# 二.动态参数
from flask import Flask, request

app = Flask(__name__)


@app.route('/cases/<int:id>/', methods=['get'], endpoint='case', redirect_to='/')              # flask哲学 /cases/ 和 /cases 是两个不同的URL，灵活
def get_case(id):
    return f'{id}'      # f -->3.6的.formart()

def index():
    return '欢迎光临'

# @app.route('/cases')
# def get_case():
#     case_id = request.args.get('id')
#     return f'{case_id}'      # f -->3.6的formart()


# 另一种注册机制，集中注册机制：2装饰器注册
app.add_url_rule('/cases', view_func=get_case)
app.add_url_rule('/', view_func=index)

print(app.url_map)
# url_map 用来存储路由关系的对象，  路由：URL和视图函数的绑定关系， 端点


if __name__ == '__main__':
    app.run(debug=True)

# flask:  1.定义的时候路径带/和不带/
#         2.装饰器注册和集中注册路由，装饰器注册也是调用add_url_rule函数
#         3.路由的常见参数：methods，endpoint,defaults,redirect_to等
#         4.大型构建循环导入问题 ，循环导入 -->解决办法：使用的时候导入 。  导入的时候如果没有使用，就import*

