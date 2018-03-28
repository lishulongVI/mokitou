# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:05
"""

from logging import config
from tornado import httpserver
from tornado import ioloop
from mokitou.app import APP
from mokitou.config.config import options

import yaml

if __name__ == '__main__':
    # 配置日志
    config.dictConfig(yaml.load(open('config/logging.yaml', 'r')))
    # 创建路由
    app = APP()
    # 创建服务
    httpServer = httpserver.HTTPServer(app)
    httpServer.bind(port=options.get('port'), address=options.get('address'))
    httpServer.start()
    ioloop.IOLoop.current().start()
