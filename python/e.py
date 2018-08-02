import requests
import webbrowser

ss = input("请输入搜索内容：")

param = {"wd": ss}

rp = requests.get('https://www.baidu.com/s', params=param)
print(rp.url)

webbrowser.open(rp.url)
