import requests
# 百度的关键词接口：'https://www.baidu.com/s?wd=keyword'
# 360的关键词接口：'https://www.so.com/s?q=keyword'
kv = {'wd': 'python'}
r = requests.get('https://www.baidu.com/s', params = kv)
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.request.url)
print(len(r.text))  # 太猛了吧？。。。。。。。

