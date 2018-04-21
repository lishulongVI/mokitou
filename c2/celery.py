# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/2 下午7:19
"""
from __future__ import absolute_import, unicode_literals
from celery import Celery
from kombu import Queue, Exchange

app_task = Celery('c2', broker='amqp://mojito:mojito@192.168.91.129:5672//vhost', include=['c2.tasks'])

app_task.conf.update(
    result_expires=3600
)

CELERY_QUEUES = {
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('task_add', Exchange('add_exchange'), routing_key='add_key'),
    Queue('task_mul', Exchange('mul_exchange'), routing_key='mul_key'),
    Queue('task_list_sum', Exchange('list_sum_exchange'), routing_key='list_sum_key'),
}

CELERY_ROUTES = {
    "task1": {
        "queue": "task_add",
        'routing_key': 'add_key'
    },
    "task2": {
        "queue": "task_mul",
        'routing_key': 'mul_key'
    },
    "task3": {
        "queue": "task_list_sum",
        'routing_key': 'list_sum_key'
    },

}

""""
1、不要用数据库作为in的amqp broker
2、使用更多的queue
3、使用具有优先级的wokers

"""

"""
what is celery ?
distribute task queue



"""
