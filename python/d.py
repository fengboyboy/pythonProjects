from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://baike.baidu.com"
his = ["/item/C%2FC%2B%2B/6824246"]

for i in range(50):

    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')

    print(soup.find('h1').get_text(), 'url:', his[-1])

    # find all sub link urls
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
        #print(his)
    else:
        his.pop()



