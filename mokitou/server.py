# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/25 上午11:05
"""
from tornado import httpserver
from tornado import ioloop
from mokitou.app import APP
from logging import config
import yaml
from mokitou.config.config import options

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
