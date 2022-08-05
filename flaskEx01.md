# flask 실습

파이썬 웹 프레임워크  : Django, Flask , Tornado, Pyramid, Bottle 등
(참조 : https://blog.naver.com/sundooedu/221340732814)

- Django Framework : 신속한 개발과 깨끗하고 실용적인 디자인을 장려하는 고수준의 파이썬 웹 프레임워크이며 장고를 사용하면 보다 빠르게 적은 코드로 더 나은 웹 응용 프로그램을 만들 수 있다.
- Flask : 작지만 강력한 파이썬 웹 프레임워크로 배우기 쉽고 짧은 시간에 웹앱 개발이 가능해 인기가 많다. Werkzeng 툴킷과 jinja2 템플릿 엔진에 기반을 두고 있다. 플라스크는 특별한 도구 또는 라이브러리가 필요 없어 마이크로 프레임워크라고 부르기도 한다.

## Flask 설치
```
pip install flask
```
flask 를 포함하여 itsdangerous, Jinja2, Werkzeug, click, MarkupSafe 등이 설치된다.

## Flask 서버 구축

```
#testflask.py  // 파일명
from flask import Flask    

app = Flask(__name__)     # 해당 모듈의 Flask 객체 생성   __name__ 현재 모듈의 이름 

@app.route('/')           # 라우팅 설정  
def run():                 
    return 'hello world'  

'''
@app.route("/profile/<username>")
def get_profile(username):
    return "profile: " + username

@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello " + username + "!</h3>"
'''

if __name__ == "__main__":# 현재 파일이 모듈이 아닌 실행파일이어야 동작
    app.run()             # app 객체 실행     app.run(host="0.0.0.0", port=80, debug=True)  
```

- 포트 확인
```
포트 검색하기
netstat /help
netstat -ano
netstat -ano | find "검색할포트번호"

프로세스 킬 
taskkill /f   /pid  프로세스ID
```

## python 날씨 flask 서버 만들기
참조 : https://blog.naver.com/starly98/221631158441

- 날씨 정보 확인
```
from urllib import request
from bs4 import BeautifulSoup

taget = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = BeautifulSoup(taget, "html.parser")

for location in soup.select("location"):
    print("도시 : ", location.select_one("city").string)
    print("날씨 : ", location.select_one("wf").string)
    print("최저 : ", location.select_one("tmn").string)
    print("최고 : ", location.select_one("tmx").string)
    print()

```

- 날씨 서버 구축
```
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    taget = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(taget, "html.parser")
    output = ""
    for location in soup.select("location"):
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨 : {}<br/>".format(location.select_one("wf").string)
        output += "최저, 최고 기온 : {}, {}".format(location.select_one("tmn").string, location.select_one("tmx").string)
        output += "<hr/>"
    return output

if __name__ == "__main__":
    app.run()     
```
