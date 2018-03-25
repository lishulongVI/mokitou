# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/22 下午5:13
"""
from tornado import ioloop
from tornado import web, httpserver
from tornado import options
import yaml
import logging

from logging import config

# name, default=None, type=None, help=None, metavar=None,
#            multiple=False, group=None, callback=None
# options.define(name='', default=None, type=None, help=None):


options.define(name='port', default=8000, type=int, help=None)
options.define(name='list', default=[], type=str, help=None, multiple=True)

"""
name 要唯一
default 选项的默认值

type 变量的类型
从命令行 或者 配置文件导入,根据类型进行转换

multiple 多参数？


help:帮助提示信息

命令行启动
➜  data_process python app_option.py --port=9000 --list='a','b','bb',

配置文件启动服务





"""


# 用来定义变量的

class IndexHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.write('<h1 align="center">你说的和你表达的不一样:app_8000</h1>')


if __name__ == '__main__':
    # 转换命令行参数
    # options.parse_command_line()
    options.parse_config_file('config.cfg')
    # options.options.logging = 'INFO'

    log_config = yaml.load(open('logging.yaml', 'r'))

    print(log_config)

    config.dictConfig(log_config)

    # print(options.options.list)
    app = web.Application([
        (r'/index', IndexHandler)
    ])
    # app.listen(port=8000, address='0.0.0.0')

    # 实例化一个httpServer
    http_server = httpserver.HTTPServer(app)

    http_server.bind(port=options.options.port, address='0.0.0.0', backlog=1024, reuse_port=True)

    http_server.start()

    # 当前线程的IOloop实例 ，这是真正的监听
    ioloop.IOLoop.current().start()

# epoll 是异步的基石

# 不建议启动多进程的问题
"""
每个子进程都会复制一个ioloop的实例
创建子进程前 修改了 ioloop ,会影响到所有的子进程


所有的进程都是由一个命令启动的
无法做到 停止服务的情况下 修改代码 ，无法修改某个进程下的代码

所有进程共享一个端口,想分别监控很难

全局参数的定义,存储 ，转换

原型，功能，参数。。。。


"""
