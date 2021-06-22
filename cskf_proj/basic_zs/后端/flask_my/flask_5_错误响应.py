from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__, template_folder='html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    file = request.files.get('pic')
    if file is None:
        return render_template('img_index.html')
    file.save(file.filename)
    return 'save success'


@app.route('/', methods=['GET', 'POST'])
def index():
    args = request.args.get('pic')
    if args is None:
        # return redirect('/login')   # login要注册一下
        return redirect(url_for('login'))  # url_for(端点,关键字参数：键=值), 一般用url_for ,传参很重要
    return 'hello'


# !!!全局错误处理--很重要
@app.errorhandler(500)
def server_error():
    return '当前访问人数较多，请耐心等候'  # 也可以return一个页面


# 如果一个函数有多个return，应保证return的类型是一致的， 可以用raise抛出异常,  abort(401,description='')封装好的可抛出的异常



if __name__ == '__main__':
    app.run(debug=True)