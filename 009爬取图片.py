import requests

path = 'C:/Users/Public/Pictures/abc.jpg'
url = 'http://image.ngchina.com.cn/2019/0523/20190523103156143.jpg'
r = requests.get(url)
print(r.status_code)
#r.encoding = r.apparent_encoding
with open(path,'wb') as f:
    f.write(r.content)
f.close()


