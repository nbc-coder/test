from bs4 import BeautifulSoup
soup = BeautifulSoup(open('C:/demo.html',encoding='utf8'),'html.parser')
print(soup.prettify())
tag = soup.a.parent
#print(tag)