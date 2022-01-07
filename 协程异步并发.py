"""
"""

import aiohttp
import asyncio
import random
from aiofile import async_open
import time
from common import get_page_urls, get_title_urls, create_path, USER_AGENT_LIST


async def async_spider(title, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={'User-Agent': random.choice(USER_AGENT_LIST)}) as resp:
            async with async_open(f'./cover/images/{title}.jpg', 'wb') as fp:
                await fp.write(await resp.read())
                print(title, url, '-->下载成功')


if __name__ == '__main__':
    create_path()
    page_urls = get_page_urls(5)
    title_urls = get_title_urls(page_urls)

    loop = asyncio.get_event_loop()

    start_time = time.time()
    tasks = [loop.create_task(async_spider(title, url)) for title, url in title_urls.items()]
    res = loop.run_until_complete(asyncio.wait(tasks))
    end_time = time.time()
    print("异步协程消耗秒数-->", end_time - start_time)
    loop.close()
