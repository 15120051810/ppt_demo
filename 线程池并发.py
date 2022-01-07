"""
线程池消耗秒数--> 2.016430139541626

"""

import time
import requests
import random
from concurrent.futures import ThreadPoolExecutor
from common import get_page_urls, get_title_urls, USER_AGENT_LIST, create_path


def save_image(title, imgae_url):
    """保存图片"""
    response = requests.get(imgae_url, headers={'User-Agent': random.choice(USER_AGENT_LIST)})
    with open(f'./cover/images/{title}.jpg', 'wb') as f:
        f.write(response.content)
        print(title, imgae_url, '-->下载成功')



def thread_pool(title_urls):
    """线程池"""

    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(save_image, title_urls.keys(), title_urls.values())


if __name__ == '__main__':
    create_path()
    page_urls = get_page_urls(5)
    title_urls = get_title_urls(page_urls)

    start_time = time.time()
    thread_pool(title_urls)
    end_time = time.time()
    print("线程池消耗秒数-->", end_time - start_time)
