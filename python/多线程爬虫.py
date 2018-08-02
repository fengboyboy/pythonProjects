from bs4 import BeautifulSoup
import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
import re

# - 定义基础URL
base_url = 'https://morvanzhou.github.io/'
# - 定义两个set记录爬过的url 和 未爬的url
unseen = set([base_url, ])
seen = set()

# - 定义两个方法 一个爬去，一个解析
# - 爬取


def crawl(url):
    response = urlopen(url)
    return response.read().decode()

# - 解析


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])
    url = soup.find('meta', {"property": "og:url"})['content']
    return title, page_urls, url


if base_url != "http://127.0.0.1:4000/":
    restricted_crawl = True
else:
    restricted_crawl = False


# -- 测试普通爬法
# count, t1 = 1, time.time()
# while len(base_url) != 0:
#     if restricted_crawl and len(seen) >= 20:
#         break
#
#     htmls = [crawl(url) for url in unseen]
#     results = [parse(html) for html in htmls]
#
#     seen.update(unseen)
#     unseen.clear()
#
#     for title, page_urls, url in results:
#         print(count, title, url)
#         count += 1
#         unseen.update(page_urls - seen)
#
# #print(seen)
# print('Total time: %.1f s' % (time.time()-t1, ))

# -- 测试分布式爬法
pool = mp.Pool(4)  # - 线程数量
count, t1 = 1, time.time()

while len(base_url) != 0:
    if restricted_crawl and len(seen) > 20:
        break

    print("crawling........")
    crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
    htmls = [j.get() for j in crawl_jobs]

    print("parswing........")
    parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
    results = [j.get() for j in parse_jobs]

    print("Analysing......")
    seen.update(unseen)
    unseen.clear()

    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        unseen.update(page_urls - seen)

print('Total time: %.1f s' % (time.time() - t1, ))    # 16 s !!!
