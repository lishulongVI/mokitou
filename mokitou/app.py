# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:08
"""
import os

from mokitou.view import index
from mokitou.config import config
from tornado import web


class APP(web.Application):
    """
    配置路由
    """

    def __init__(self):
        handlers = [
            # (r'/', index.IndexHandler),
            (r'/home', index.HomeHandler),
            (r'/article', index.ArticalHandler, dict(page=1)),
            web.url(
                r'/redirect',
                index.RedirectHandler,
                dict(name='lishulong', age=23), name='info'
            ),
            (r'/video/(\w+)/(\w+)', index.VideoHandler),
            (r'/video/p/(?P<pid>\w+)/(?P<cid>\w+)', index.VideoHandler1),
            (r'/register', index.RegisterHandler),
            # http://localhost:9000/video/lishulong?pid=葛优&cid=上一个当
            (r'/video/lishulong', index.LishulongHandler),
            (r'/profile', index.ProfileHandler),
            (r'/file', index.FileHandler),
            (r'/trans', index.TranceHandler),
            (
                r'/(.*)$', web.StaticFileHandler,
                dict(
                    path=os.path.join(config.base_path, 'statics/html'),
                    default_filename='index.html')
            ),
        ]
        # super().__init__(handlers=handlers, settings=config.settings)
        super().__init__(handlers, **config.settings)
