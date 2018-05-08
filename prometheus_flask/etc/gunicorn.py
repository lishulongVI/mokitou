# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/5/8 上午10:46
"""
import multiprocessing

import gevent.monkey

gevent.monkey.patch_all()

bind = '0.0.0.0:10000'

max_requests = 10000

keepalive = 5

backlog = 2048

proc_name = 'test'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

loglevel = 'info'
timeout = 90
errorlog = '-'

def worker_exit(server, worker):
    from prometheus_client import multiprocess
    multiprocess.mark_process_dead(worker.pid)
