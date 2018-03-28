# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/23 下午2:07
"""

import multiprocessing
import random

print(multiprocessing.cpu_count())


class Test(object):
    """
    一个星（*）：表示接收的参数作为元组来处理

    两个星（**）：表示接收的参数作为字典来处理
    """

    def get_dict(self, **dicts):
        """"""
        for i in dicts:
            print(i)

    def get_tuple(self, *t):
        print(t)


if __name__ == '__main__':
    t = (1, 2, 3)

    print(Test().get_tuple(*t))

    d = {
        'name': 'name',
        'age': 12,
    }

    print(Test().get_dict(**d))

    print(random.randint(20000, 30000))
    print(random.randint(20000, 30000))
    print(random.randint(20000, 30000))
