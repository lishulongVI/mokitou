# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/8 下午2:55
"""
import asyncio
import aiohttp


async def fetch_response(session, url):
    response = await session.get(url)

    if response.status == 200:
        return await response.text()
    else:
        return None


loop = asyncio.get_event_loop()

session = aiohttp.ClientSession(loop=loop)

tasks = [
    asyncio.ensure_future(fetch_response(session, 'http://192.168.91.129:8080/#/queues')),
    asyncio.ensure_future(fetch_response(session, 'https://movie.douban.com/subject/26969821/'))
]

loop.run_until_complete(asyncio.wait(tasks))

print(tasks[0]._result)
print(tasks[1]._result)


if session.closed:
    session.close()
    loop.close()
