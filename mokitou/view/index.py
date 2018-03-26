# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:08
"""
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write(u'这是index 页面<link rel="stylesheet" href="/static/index.js">')
        url = self.reverse_url('info')
        print(url)
        self.write("<a href='{}'> another page info about user</a>".format(url))
        self.finish()


class HomeHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write(r'//一江春水向东流//')


class ArticalHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def initialize(self, page):
        self.page = page

    def get(self, *args, **kwargs):
        # self.set_header('content-type', 'application/json;charset=utf-8')
        name = self.get_query_argument("name")
        res = dict(page=self.page, artical_name="mokitou", content="鸡尾酒", tip=name)
        self.write(res)


class RedirectHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        print(kwargs)
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')

    def initialize(self, name, age):
        # self.name = name
        # self.age = age
        pass

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        # 反向解析
        self.write(dict(userName=self.name, age=self.age))


class VideoHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, u1, u2, *args, **kwargs):
        self.write('video u1:{} u2:{}'.format(u1, u2))
