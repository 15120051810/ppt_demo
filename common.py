import os
import requests
import random
from bs4 import BeautifulSoup

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6'
]

get_page_urls = lambda x: [f"https://www.miaoshou.net/video/list_0_0_3_{page}.html" for page in range(1, x + 1)]


def get_title_urls(urls):
    """
    1 解析每页各个视频的文本标题
    2 提取每页各个视频封面的url
    """
    title_url = {}
    for url in urls:
        response = requests.get(url, headers={'User-Agent': random.choice(USER_AGENT_LIST)})
        soup = BeautifulSoup(response.content.decode(), 'lxml')
        div_content = soup.select('ul[class="list_ul ovH"] li')
        for i in div_content:
            image_url = i.select('img')[0].get('src')
            title = i.select('p[class="bt_title text_over1 mt15 fs16 mb30 color38"]')[0].get_text()
            title_url[title] = image_url
    return title_url


def create_path():
    """创建目录"""
    page_dir = os.path.abspath(os.path.join(__file__, f'../cover/images'))
    if not os.path.exists(page_dir):
        os.mkdir(page_dir)



if __name__ == '__main__':
    create_path()

    page_urls = get_page_urls(5)
    print('page_urls', page_urls) # ['https://www.miaoshou.net/video/list_0_0_3_1.html', 'https://www.miaoshou.net/video/list_0_0_3_2.html']

    title_urls = get_title_urls(page_urls)
    print('title_urls', title_urls, len(title_urls))
