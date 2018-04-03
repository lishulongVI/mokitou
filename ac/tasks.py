# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/3 上午10:59
"""

from ac.celery import app_task


@app_task.task
def add(x, y):
    return x + y


@app_task.task
def mul(x, y):
    return x * y


@app_task.task
def list_sum(x: list):
    return sum(x)


"""
>>> from ac.tasks import list_sum
>>> list_sum.delay([12,23,45])
<AsyncResult: 60d1b1b4-41c5-4dea-a11c-3b9233496fdd>
>>> list_sum.delay([12,23,45])
<AsyncResult: 19b0d59e-db57-4092-89fb-c354c417f3d5>


"""

"""
monitor celery task
flower -A ac --port=9999 --address=0.0.0.0 --broker_api=http://mojito:mojito@192.168.91.129::15672/api/ --broker=amqp://mojito:mojito@192.168.91.129:5672//

"""
