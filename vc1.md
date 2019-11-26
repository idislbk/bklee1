# 웹크롤링 

1 . BeautifulSoup4, requests 설치

웹 페이지를 가져올 수 있는 requests 모듈과, 가져온 웹 페이지를 분석해서 우리가 원하는 정보를 추출해줄 BeautifulSoup4를 설치합시다.

```
윈도우에서의 설치 명령어  
pip install requests   
pip install BeautifulSoup4  
```

## 제목 가져오기
```
import requests
from bs4 import BeautifulSoup

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청 
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('http://v.media.daum.net/v/20170615203441266')

# print(res.content)
# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(res.content, 'html.parser')

# 3) 필요한 데이터 검색
title = soup.find('title')

# 4) 필요한 데이터 추출
print(title.get_text())
```

## 날씨 미세먼지 가져오기
```
# 날씨 미세먼지 가져오기
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#print(html.text)
soup = bs(html.text,'html.parser')

data1 = soup.find('div',{'class':'detail_box'})   #첫번째 것만 찾음
print(data1)
data2 = data1.findAll('dd')                       #모두 찾음 : 배열로
print('---------------------------------------------------')
print(data2)

fine_dust = data2[0].find('span',{'class':'num'}).text
print(fine_dust)

ultra_fine_dust = data2[1].find('span',{'class':'num'}).text
print(ultra_fine_dust)
```

