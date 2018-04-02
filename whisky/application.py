# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/2 上午10:07
"""
from tornado.web import Application
from whisky.config.settings import settings
from whisky.controllers import *

"""
tornado.httpclient.AsyncHttpClient 
tornado 提供的异步web请求客户端，用来进行异步web请求

fetch(request,callback=None)
用来执行一个web请求，并异步响应返回一个tornado.httpclient.HttpResponse

request 可以是一个url，也可以是一个tornado.httpclient.httpRequest


HttpRequest:
http 请求类，改类的构造函数可以接受参数

url：
method：
headers：
body：



HttpResponse http响应累


code：

reason：code  desc

body：
error：





"""


class APP(Application):
    def __init__(self):
        handlers = [
            (r'/', EmailHandler),
            (r'/chat', ChatHandler),
            (r'/index', IndexHandler),
        ]
        super().__init__(handlers, **settings)
