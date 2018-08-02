# 下载图片

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re

# 1.先找到网页中需要下载的图片的地址
web_url = "https://morvanzhou.github.io/tutorials/data-manipulation/scraping/3-02-download/"

html = urlopen(web_url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')



imgs_url = soup.find("a", {"href": re.compile("/static/img/(.*?\.png)")})
print(imgs_url)
urls = soup.find("a")

