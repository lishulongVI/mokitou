# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/9 上午11:53
"""

import traceback
import logging

logger = logging.getLogger(__file__)

spc_check_overdue_cnt = {
    'name': "info"
}

try:
    a = 1 / 0
except Exception as e:
    logger.exception('error:{},content:{} ,spc_check_overdue_cnt:{}'.
                     format(e, traceback.format_exc(), spc_check_overdue_cnt))

print('aas')
