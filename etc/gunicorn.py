# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/3 下午9:28
"""
# -*- coding:utf-8 -*-

import multiprocessing

import gevent.monkey

gevent.monkey.patch_all()

bind = "0.0.0.0:8000"
max_requests = 10000

keepalive = 5
backlog = 2048

proc_name = 'proceess name'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

loglevel = 'info'
timeout = 90
errorlog = '-'

"""

/anaconda/envs/tornado/bin/gunicorn -b 0.0.0.0:10002  -c  /etc/gunicorn.py server:app

"""