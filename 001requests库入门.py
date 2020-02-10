import requests
r = requests.get('http://www.baidu.com')
print(r.status_code)
r.encoding = 'utf-8'
print(r.text)
print(type(r))
print(r.headers)
print(r.encoding)
print(r.apparent_encoding)