"""
多线程消耗秒数--> 0.5908217430114746
"""

import time
import threading
import requests
import random
from common import get_page_urls, get_title_urls, USER_AGENT_LIST, create_path


def save_image(title, imgae_url):
    """保存图片"""
    response = requests.get(imgae_url, headers={'User-Agent': random.choice(USER_AGENT_LIST)})
    with open(f'./cover/images/{title}.jpg', 'wb') as f:
        f.write(response.content)
        print(title,imgae_url,'-->下载成功')



def multi_thread(title_urls):
    """多线程爬取指定页数"""

    threads = []
    for title, url in title_urls.items():
        threads.append(threading.Thread(target=save_image, args=(title, url)))

    [thread.start() for thread in threads]
    [thread.join() for thread in threads]


if __name__ == '__main__':
    create_path()
    page_urls = get_page_urls(1)
    title_urls = get_title_urls(page_urls)



    start_time = time.time()
    multi_thread(title_urls)
    end_time = time.time()

    print("多线程消耗秒数-->", end_time - start_time)
