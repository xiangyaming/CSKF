# -*- coding:utf-8 -*-
# @FileName  :本地服务.py
# @Time      :2021/4/22 0022 00:53
# @Author    :xiaoming
# -----------------------------------------------------

import flask
from flask import jsonify

app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return jsonify({"code":1, "msg":"hello world"})

if __name__ == '__main__':
    app.run(debug=True)