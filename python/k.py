from bs4 import BeautifulSoup
import requests

URL = "http://www.ivsky.com/tupian/ziranfengguang/"


# - 获取网页文本
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
images_urls = soup.find_all("ul", {"class": "ali"})
#print(images_urls)

for ul in images_urls:
    imgs = ul.find_all('img')
    #print(imgs)
    for img in imgs:
        url = img['src']
        print(url)
        r = requests.get(url, stream=True)
        imagename = url.split('/')[-1]
        with open('./imgs/%s' % imagename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                 f.write(chunk)
        print('Save : %s' % imagename)
