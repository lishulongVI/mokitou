# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/2 上午10:13
"""
import tornado
from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient


class EmailHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def on_response(self, response):
        if response.error:
            self.send_error(500)
        else:
            data = str(response.body, encoding='utf-8')
            self.write(data)
        self.finish()

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        """
        @tornado.web.asynchronous 不关闭通信的通道
        :param args:
        :param kwargs:
        :return:
        """
        client = AsyncHTTPClient()
        url = "https://www.bilibili.com"
        client.fetch(url, self.on_response)
        self.write('ok')
