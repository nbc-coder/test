import requests
r = requests.get('https://item.jd.com/100009177368.html#crumb-wrap')
print(r.status_code)
print(r.encoding)
print(r.text[:200])  # 太猛了吧？。。。。。。。

