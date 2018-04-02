# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/2 上午11:12
"""
from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render('../templates/chat.html')


class ChatHandler(WebSocketHandler):
    """
    处理通信
    """
    users = []

    def check_origin(self, origin):
        """
        判断源，对于符合条件的请求 允许链接
        :param origin:
        :return:
        """
        return True

    def on_message(self, message):
        """
        当客户端发送消息过来时候调用
        :param message:
        :return:

        """
        for user in self.users:
            user.write_message(u'{} tell:{}'.format(self.request.remote_ip, message))

        pass

    def data_received(self, chunk):
        pass

    def open(self, *args, **kwargs):
        """
        当客户端链接创建后呗调用
        :param args:
        :param kwargs:
        :return:
        """
        self.users.append(self)
        print(self.users)
        for user in self.users:
            # 主动向客户端发送mesg消息，
            user.write_message(u'{} login...'.format(self.request.remote_ip))

    def on_close(self):
        """
        当websocket 链接关闭后调用
        :return:
        """
        self.users.remove(self)
        for user in self.users:
            # 主动向客户端发送mesg消息，
            user.write_message(u'{} logout...'.format(self.request.remote_ip))
