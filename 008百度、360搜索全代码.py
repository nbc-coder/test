import requests
keyword = "python"
try:
    kv = {'q': keyword}
    r = requests.get('https://www.so.com/s', params = kv)
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.request.url)
    r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
    print(len(r.text))
except:
    print('爬取失败')


