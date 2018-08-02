import requests


file = {'uploadFile': open('./51c2f02a7afdd.jpg', 'rb')}

r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)

print(r.text)
