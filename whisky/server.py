# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/2 上午10:03
"""
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from whisky.application import APP
from whisky.config.settings import options

if __name__ == '__main__':
    app = APP()

    http_server = HTTPServer(app)

    http_server.bind(port=options.get('port'), address=options.get('address'))

    http_server.start()

    IOLoop.current().start()
