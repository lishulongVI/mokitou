# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/29 下午4:44
"""
import asyncio


async def async_demo():
    print('......')
    res = await asyncio.sleep(10)
    print(res)
    print('........')


@asyncio.coroutine
def hello():
    print('begin.....')

    r = yield from asyncio.sleep(10)
    print('end.....')


# async_demo()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_demo())
    loop.close()
