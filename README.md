# 파이썬 개요

- 파이썬 URL : https://www.python.org/downloads/
- 파이썬 + 아나콘다 + VSCode 연동 : https://daily-error.tistory.com/14
- 파이썬 VS 아나콘다 차이점 
  : http://snowdeer.github.io/python/2017/11/07/python-vs-anaconda/
- 파이썬 도움되는 사이트 : https://wikidocs.net/
- 파이썬/웹크롤링 강좌 : https://www.fun-coding.org/crawl_basic2.html

아나콘다는 파이썬 + Scipy + numpy + pandas + matplotlib + spyder + jupyternotebook 등등을 같이 깔아준다.
파이썬과 아나콘다를 같이 설치하면 경로(환경변수) 등이 꼬여 오류발생할 수 있다고 하니 고려하여 하나만 깔아줄 것.

> Python에서의 가상 환경이란?
```
파이썬에서는 한 라이브러리에 대해 하나의 버전만 설치가 가능합니다.
여러개의 프로젝트를 진행하게 되면 이는 문제가 됩니다. 작업을 바꿀때마다 다른 버전의 라이브러리를 설치해야합니다.
이를 방지하기 위한 격리된 독립적인 가상환경을 제공합니다.
일반적으로 프로젝트마다 다른 하나의 가상환경을 생성한 후 작업을 시작하게 됩니다.
가상환경의 대표적인 모듈은 3가지가 있습니다.
venv : Python 3.3 버전 이후 부터 기본모듈에 포함됨
virtualenv : Python 2 버전부터 사용해오던 가상환경 라이브러리, Python 3에서도 사용가능
conda : Anaconda Python을 설치했을 시 사용할 수있는 모듈
pyenv : pyenv의 경우 Python Version Manger임과 동시에 가상환경 기능을 플러그인 형태로 제공
``` 

>[아나콘다/파이썬 + 가상환경구성]
1. 많이 보이는 방법 : virtualenv
```
> pip install virtualenv
> virtualenv c:\만들고자 하는 폴더이름(이하 방이름)
> cd c:\방이름\scripts
> activate    하면 실행됨
> deactivate 하면 나가짐
```

