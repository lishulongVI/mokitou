# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:08
"""
from tornado.web import Application
from .view import index
from mokitou.config import config
from tornado import web


class APP(Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/home', index.HomeHandler),
            (r'/article', index.ArticalHandler, dict(page=1)),
            web.url(r'/redirect', index.RedirectHandler, dict(name='lishulong', age=23), name='info'),
            (r'/video/(\w+)/(\w+)', index.VideoHandler)
        ]
        super().__init__(handlers=handlers, settings=config.setting)
        # super().__init__(handlers, **config.setting)
