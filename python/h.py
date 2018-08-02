# POST 登录 cookies login

import requests

link_url = 'http://pythonscraping.com/pages/cookies/welcome.php'
dd = {'username': 'aa', 'password': 'password'}

r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=dd)
print(r.cookies.get_dict())

r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)
