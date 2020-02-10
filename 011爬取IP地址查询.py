import requests
url = 'http://m.ip138.com/ip.asp?ip='
r = requests.get(url+'117.150.32.22')
print(r.status_code)
print(r.text[:1000]) 

