# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/3 上午10:37
"""
from celery_task.celery_progress.backend import Progress


def get_progress(task_id):
    progress = Progress(task_id=task_id)
    return progress.get_info()
