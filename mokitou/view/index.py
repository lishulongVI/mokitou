# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:08
"""
import json
from tornado.web import RequestHandler

from mokitou.dao.orm.ArticleDao import Article
from mokitou.utils.json_util import JsonEncoder


class IndexHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write(u'这是index 页面<link rel="stylesheet" href="/statics/index.js">')
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


class VideoHandler1(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, pid, cid, *args, **kwargs):
        self.write('video u1:{} u2:{}'.format(pid, cid))


class RegisterHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        pass


class LishulongHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        pid = self.get_query_argument('pid')
        cid = self.get_query_argument('cid')
        self.write('video u1:{} u2:{}'.format(pid, cid))


class ProfileHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def prepare(self):
        """
        预处理方法，在执行对应的请求方法之前调用
        任何一种http请求都会执行prepare方法
        :return:
        """
        pass

    def get(self, *args, **kwargs):
        def p(a, b):
            return '{}-{}'.format(a, b)

        self.render('../templates/profile.html', args=dict(name='lishulong', password='passwd'), p=p)

    def post(self, *args, **kwargs):
        userName = self.get_body_argument('userName')
        password = self.get_body_argument('password')
        hobbyes = self.get_body_arguments('hobby')

        self.write(dict(userName=userName, password=password, hobbyes=hobbyes))


from mokitou.config.config import base_path
import os


class FileHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render('../templates/file.html')

    def post(self, *args, **kwargs):
        """
            self.request.files = {
                'file': [
                    {
                        "filename": 'name',
                        "body": 'body',
                        "content_type": 'content_type',
                    }
                ],

                'imge': [
                    {
                        {
                            "filename": 'name',
                            "body": 'body',
                            "content_type": 'content_type',
                        }
                    }
                ]
            }
        :param args:
        :param kwargs:
        :return:
        """
        # filename
        #
        files = self.request.files
        for f in files:
            for b in files.get(f):
                fp = os.path.join(base_path, 'upfile/{}'.format(b.filename))
                with open(fp, 'wb') as b_f:
                    b_f.write(b.body)
        pass


class DealHandler(RequestHandler):
    """
    正常处理流程
    """

    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def prepare(self):
        pass

    def get(self, *args, **kwargs):
        pass

    def on_finish(self):
        pass


class ERRORHandler(RequestHandler):
    """
    异常处理流程
    """

    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def prepare(self):
        pass

    def get(self, *args, **kwargs):
        pass

    def set_default_headers(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

    def on_finish(self):
        pass


class TranceHandler(RequestHandler):
    """
    自动转义，防止恶意提交
    关闭自动转义
    """

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        s = '<h1>hello word</h1>'
        self.render('../templates/index.html', index=s)


class ArticleHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        self.set_header('Content-type', 'application/json')

    def get(self, *args, **kwargs):
        sql = 'select * from article'
        res = self.application.db.get_all(sql=sql)
        print(res)
        self.write(json.dumps(res, cls=JsonEncoder))

    def put(self, *args, **kwargs):
        name = self.get_body_argument('name')
        content = self.get_body_argument('content')
        sql = 'INSERT INTO article(article_name, article_content) VALUES("{}", "{}")'.format(name, content)
        res = self.application.db.upsert_record(sql)
        print(res)
        self.write(dict(result=res))

    def patch(self, *args, **kwargs):
        article = Article('llll', 'content')
        self.write(dict(result=article.save_obj()))
