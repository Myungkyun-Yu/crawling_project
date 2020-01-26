from bs4 import BeautifulSoup

html = """
    <html>
        <head>
            <body>
                <h1 id='title'> (1) 크롤링이란 </h1>
                <p class='cssstyle'> 웹 페이지에서 데이터를 추출하는 것 </p>
                <p id='body' align='center'> 파이썬을 중심으로 다양한 크롤링이 발달함 </p>
            </body>
        </head>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')
# mydata = soup.find(id='title')
# mydata = soup.find('p', class_='cssstyle')
# mydata = soup.find('p', 'cssstyle')
# mydata = soup.find('p', attrs={'align': 'center'})
mydata = soup.find('p', attrs={'id': 'body', 'align': 'center'})
# mydata = soup.find(id='body')
print(mydata.get_text())

# find_all 은 해당 태그에 속한 모든 값을 가져온다
# find_all 을 사용하기 위해서는 리스트에 담아야 하기 때문에 for 문을 사용해서 값을 하나씩 저장하여 출력한다.
# mydata = soup.find_all('p')
# for item in mydata:
#   print(item.get_text())