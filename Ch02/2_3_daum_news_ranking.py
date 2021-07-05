"""
날짜 : 2020/12/28
이름 : 김하린
내용 : 다음 뉴스 파싱(parsing)하기
"""

import requests as req
from bs4 import BeautifulSoup as bs

# 다음 뉴스 페이지 요청
response = req.get('https://news.daum.net/ranking/popular')


# 다음 뉴스 페이지 1~10위까지 파싱
dom = bs(response.text, 'html.parser')
titles = dom.select('ul.list_news2 div.cont_thumb a')

# 1~10위까지 데이터 출력
for i in range(10):
    print(titles[i].text)
