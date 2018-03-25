# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:08
"""
from tornado.web import Application
from .view import index
from mokitou.config import config


class APP(Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/home', index.HomeHandler),
        ]
        super().__init__(handlers=handlers, settings=config.setting)
        # super().__init__(handlers, **config.setting)
