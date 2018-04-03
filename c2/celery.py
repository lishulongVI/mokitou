# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/2 下午7:19
"""
from __future__ import absolute_import, unicode_literals
from celery import Celery
from kombu import Queue, Exchange

app_task = Celery('c2', broker='amqp://mojito:mojito@192.168.91.129:5672//', include=['c2.tasks'])

app_task.conf.update(
    result_expires=3600
)

celery_queues = {
    Queue('default', Exchange('default'), routing_key='default')
}
