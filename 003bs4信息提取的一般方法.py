from bs4 import BeautifulSoup
soup = BeautifulSoup(open('C:/demo.html',encoding='utf8'),'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))