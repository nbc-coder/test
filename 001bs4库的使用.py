import requests
r = requests.get('https://python123.io/python/knight_web/5e1bdac686a54b186fa04d07')
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.text[:1000]) 

demo = r.text[:1000]
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())