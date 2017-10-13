#!/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask_script import Manager

app = Flask(__name__)
# 命令行参数启动
manager = Manager(app)

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your Browser is %s!</p>' % user_agent


# @app.route('/')
# def index():
#     return '<h1>Bad Request</h1>', 400


# @app.route('/')
# def index():
#    response = make_response('<h1>This is a docment !</h1>')
#    response.set_cookie('ans', '222')
#    return response

@app.route('/')
def index():
    return redirect('http://www.baidu.com')


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s !</h1>' % name

# if __name__ == '__main__':
#     app.run(debug=True)


if __name__ == '__main__':
    manager.run()


