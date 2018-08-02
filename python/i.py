
# session登录

import requests

session = requests.Session()

payload = {'username': 'aa', 'password': 'password'}

r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)

print(r.cookies.get_dict())


r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)



