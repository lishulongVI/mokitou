# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/29 下午6:23
"""
import time
import threading


def consumer(callback):
    def run(cb):
        print('start....')
        time.sleep(5)
        cb('this is data')
        print('end....')

    threading.Thread(target=run, args=(callback,)).start()


def finish(data):
    print('start callback....')
    print('data:{}....'.format(data))
    print('end callback....')


consumer(finish)
consumer(finish)
