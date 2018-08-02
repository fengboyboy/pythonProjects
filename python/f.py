
import requests


data = {'firstname': 'a', 'lastname': 'b'}

r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)

print(r.text)

