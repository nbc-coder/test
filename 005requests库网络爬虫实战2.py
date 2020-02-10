import requests
kv = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.amazon.cn/dp/B01M68PABD/ref=sr_1_8?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=1DD9SBLNXZ39L&keywords=%E7%BC%96%E7%A8%8B%E4%B9%A6%E7%B1%8D&qid=1581241906&s=amazon-global-store&sprefix=%E7%BC%96%E7%A8%8B%E4%B9%A6%2Camazon-global-store%2C186&sr=8-8'
r = requests.get(url,headers = kv)
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.encoding)
print(r.request.headers)
print(r.text[:200])  # 太猛了吧？。。。。。。。

