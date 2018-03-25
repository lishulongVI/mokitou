# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/22 下午5:13
"""
from tornado import ioloop
from tornado import web, httpserver


class IndexHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write('<h1 align="center">你说的和你表达的不一样</h1>')


if __name__ == '__main__':
    app = web.Application([
        (r'/index', IndexHandler)
    ])
    app.listen(port=8000, address='0.0.0.0')

    # 实例化一个httpServer
    # http_server = httpserver.HTTPServer(app)
    #
    # http_server.bind(port=8000, address='0.0.0.0', backlog=1024, reuse_port=True)
    #
    # http_server.start(1)

    # 4+1 -1 None
    #
    # 当前线程的IOloop实例 ，这是真正的监听
    ioloop.IOLoop.current().start()
