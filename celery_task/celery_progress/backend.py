# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/3 上午9:59
"""
from abc import ABCMeta, abstractclassmethod

from decimal import Decimal

from celery.result import AsyncResult

PROGRESS_STATE = 'PROGRESS'


class AbstractProgressRecorder(object):
    __metaclass__ = ABCMeta

    @abstractclassmethod
    def set_progress(self, current, total):
        pass


class ConsoleProgressRecorder(AbstractProgressRecorder):
    def __init__(self, task):
        self.task = task

    def set_progress(self, current, total):
        percent = round(Decimal(current) / Decimal(total) * Decimal(100), 2) if total > 0 else 0

        self.task.update_state(
            state=PROGRESS_STATE,
            meta={
                'current': current,
                'total': total,
                'percent': percent
            }
        )
        pass


class Progress(object):
    def __init__(self, task_id):
        self.task_id = task_id
        self.result = AsyncResult(task_id)

    def get_info(self):
        if self.result.ready():
            return dict(complete=True, success=self.result.successful(), progress=_get_completed_progress())
        elif self.result.state == PROGRESS_STATE:
            return dict(complete=False, success=None, progress=self.result.info)
        elif self.result.state in ['PENDING', 'STARTED']:
            return dict(complete=False, success=None, progress=_get_unknown_progress())
        else:
            return self.result.info


def _get_completed_progress():
    return dict(current=100, total=100, precent=100)


def _get_unknown_progress():
    return dict(current=0, total=100, percent=0)
