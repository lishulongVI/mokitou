# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/29 下午6:23
"""
import time
import threading

gen = None


def log_io():
    print('log_io start.....')
    time.sleep(5)
    print('log end ....')
    yield 'data....ss.....ssd...'


# def send(data):
#     print('start call back .....')
#
#     print('accept data:{}'.format(data))
#     time.sleep(4)
#     print('end call back .....')
#     return data


def genCoroutine(fuc):
    def wrapper(*args, **kwargs):
        gen = fuc()
        gen2 = next(gen)

        def run(g):
            res = next(g)
            try:
                gen.send(res)
            except StopIteration as e:
                pass

        threading.Thread(target=run, args=(gen2,)).start()

    return wrapper


@genCoroutine
def request_1():
    print('request_1 start.....')
    re = yield log_io()
    print('1data:{}'.format(re))
    print('request_1 end .....')


@genCoroutine
def request_2():
    print('request_2 start.....')
    re = yield log_io()
    print('2data:{}'.format(re))
    print('request_2 end .....')


def main():
    request_1()
    request_2()
    request_2()
    pass


main()
