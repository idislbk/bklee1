# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:51:27 2019

@author: 6001100
"""

from flask import Flask  ,render_template  #, url_for

app = Flask(__name__)     # 해당 모듈의 Flask 객체 생성   __name__ 현재 모듈의 이름 

@app.route('/')           # 라우팅 설정  
def run():                 
    return 'hello world'  


@app.route("/profile/<username>")
def get_profile(username):
    return "profile: " + username

@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello " + username + "!</h3>"


@app.route('/test1')
def hello():
    return render_template('test1.html')

@app.route('/test/<name>')
def hello1(name):
    return render_template('test/'+ name )

if __name__ == "__main__":# 현재 파일이 모듈이 아닌 실행파일이어야 동작
    app.run()             # app 객체 실행