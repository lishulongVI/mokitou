# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/2 下午7:19
"""
from celery import Celery

app_task = Celery('ac', broker='amqp://mojito:mojito@192.168.91.129:5672//', include=['ac.tasks'])

app_task.conf.update(
    result_expires=3600
)
