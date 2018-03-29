# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/28 下午4:40
"""
import json
import datetime


class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        else:
            return super().default(o)
