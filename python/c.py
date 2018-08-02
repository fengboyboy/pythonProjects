# -- 获取图片链接

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# -- 获取html网页
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
#print(html)

# -- 解析html
soup = BeautifulSoup(html, features='lxml')
#print(soup)

# -- 查找links 
imglinks = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
#print(imglinks)

for imglink in imglinks:print(imglink['src'])

