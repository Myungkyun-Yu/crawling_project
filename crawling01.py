# python 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.bloter.net/archives/368941')
soup = BeautifulSoup(res.content, 'html.parser')

mydata = soup.find('div', 'entry-content')
print(mydata.get_text())

