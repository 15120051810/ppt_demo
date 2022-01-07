"""
单线程爬取消耗秒数--> 14.707400798797607
"""

import time
import random
import requests
from common import get_page_urls, get_title_urls, USER_AGENT_LIST, create_path


def save_image(title, imgae_url):
    """保存图片"""
    response = requests.get(imgae_url, headers={'User-Agent': random.choice(USER_AGENT_LIST)})

    with open(f'./cover/images/{title}.jpg', 'wb') as f:
        f.write(response.content)


def single_spider(title_urls):
    """单线程顺序爬取指定页数"""

    for i, title_url in enumerate(title_urls.items(), 1):
        save_image(*title_url)
        print(i, title_url[0], title_url[1], '下载成功')


if __name__ == '__main__':
    create_path()
    page_urls = get_page_urls(5)
    title_urls = get_title_urls(page_urls)
    # print(page_urls,title_urls)

    start_time = time.time()
    single_spider(title_urls)
    end_time = time.time()

    print("单线程爬取消耗秒数-->", end_time - start_time)
