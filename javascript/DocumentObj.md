# [Document 객체](https://opentutorials.org/course/1375/6740)

> Document 객체는 DOM의 스팩이고 이것이 웹브라우저에서는 HTMLDocument 객체로 사용된다. HTMLDocument 객체는 문서 전체를 대표하는 객체라고 할 수 있다

![](https://github.com/idislbk/bklee1/blob/master/javascript/img/DocumentObject.PNG)

```html
<script>
//document 객체는 window 객체의 소속이다.
console.log(window.document);
//document 객체의 자식으로는 Doctype과 html이 있다. 
console.log(window.document.childNodes[0]);
console.log(window.document.childNodes[1]);
</script>
```

### 주요 API

- 노드 생성 API
    - createElement()
    - createTextNode()

- 문서 정보 API
    - title
    - URL
    - referrer
    - lastModified  

<br />

---

# [Text 객체](https://opentutorials.org/course/1375/6744)
> 텍스트 객체는 텍스트 노드에 대한 DOM 객체로 CharcterData를 상속 받는다. 

![](https://github.com/idislbk/bklee1/blob/master/javascript/img/TextObject.PNG)

```html
<p id="target1"><span>Hello world</span></p>
<p id="target2">
    <span>Hello world</span>
</p>
<script>
var t1 = document.getElementById('target1').firstChild;
var t2 = document.getElementById('target2').firstChild;
 
console.log(t1.firstChild.nodeValue);
try{
    console.log(t2.firstChild.nodeValue);   
} catch(e){
    console.log(e);
}
console.log(t2.nextSibling.firstChild.nodeValue);
 
</script>
```
결과
```
Hello world
TypeError {stack: (...), message: "Cannot read property 'nodeValue' of null"}
Hello world
```
### 주요 기능

- 텍스트 노드 가져오는 API
    - data
    - nodeValue

- 조작
    - appendData()
    - deleteData()
    - insertData()
    - replaceData()
    - subStringData()  
- 생성
    - [docuemnt.createTextNode()](https://opentutorials.org/module/904/6701)

------

## [값 API](https://opentutorials.org/course/1375/6745)

- data
- nodeValue

```html
<ul>
    <li id="target">html</li> 
    <li>css</li>
    <li>JavaScript</li>
</ul>
<script>
    var t = document.getElementById('target').firstChild;
    console.log(t.nodeValue);
    console.log(t.data);
</script>
```

------
## [조작 API](https://opentutorials.org/course/1375/6746)
> 텍스트 노드가 상속 받은 CharacterData 객체는 문자를 제어할 수 있는 다양한 API를 제공
- appendData()
- deleteData()
- insertData()
- replaceData()
- subStringData() 

> 예제
>> [샘플소스](https://github.com/idislbk/bklee1/blob/master/javascript/templates/test/text_test2.html)
    <br />
>> [Test Url](https://idislbk.github.io/bklee1/javascript/templates/test/text_test2.html) : https://idislbk.github.io/bklee1/javascript/templates/test/text_test2.html 

<br />

---

# [문서의 기하학적 특성](https://opentutorials.org/course/1375/7112)

요소의 크기와 위치

![](https://github.com/idislbk/bklee1/blob/master/javascript/img/boxModel.PNG)  
[*css 박스모델* ]


```html
<style>
   body{
        padding:0;
        margin:0;
    }
    #target{
        width:100px;
        height:100px;
        border:50px solid #1065e6;
        padding:50px;
        margin:50px;
    }
</style>
<div id="target">
    Coding
</div>
<script>
var t = document.getElementById('target');
console.log(t.getBoundingClientRect());
</script>
```
#### **<예제>**
- [샘플소스](https://github.com/idislbk/bklee1/blob/master/javascript/templates/test/text_test3.html)
    - [[실행]](https://idislbk.github.io/bklee1/javascript/templates/test/text_test3.html) 
    - test url : https://idislbk.github.io/bklee1/javascript/templates/test/text_test3.html
    - local url: http://localhost:5000/test/text_test3.html 
- [중첩 예제소스](https://idislbk.github.io/bklee1/javascript/templates/javascript/templates/test/text_test4.html)
    - [[실행]](https://idislbk.github.io/bklee1/javascript/templates/test/text_test4.html) 
    - test url: https://idislbk.github.io/bklee1/javascript/templates/test/text_test4.html 
    - local url: http://localhost:5000/test/text_test4.html 


>  - 오래된 브라우저에서는 getBoundingClientRect를 지원하지 않을 수 있기 때문에 
이런 경우 offsetLeft와 offsetTop 프로퍼티를 사용한다.
>  - 테두리를 제외한 엘리먼트의 크기를 알고 싶다면  ClientWidth, ClientHeight를 사용

```html
<script>
var t = document.getElementById('target');
console.log('clientWidth:', t.clientWidth, 'clientHeight:', t.clientHeight);
</script>
```

### Viewport
> 요소의 위치를 생각할 때는 사실 조금 더 복잡해진다. 문서가 브라우저의 크기보다 큰 경우는 스크롤이 만들어지는데 스크롤에 따라서 위치의 값이 달라지기 때문이다. 이를 이해하기 위해서는 우선 viewport에 대한 이해가 선행되어야 한다. 
- **viewport** : 사용자가 웹페이지에서 볼수있는 가시영역

![](https://github.com/idislbk/bklee1/blob/master/javascript/img/viewport.PNG)  

- viewport의 좌표    
    - Element.getBoundingClientRect() : 요소의 크기와 요소의 viewport에서의 상대적인 위치를 반환
    - pageYOffset : 브라우저의 문서 위치 Y값을 반환 (스크롤의 정도 확인)
    - [[실행]](https://idislbk.github.io/bklee1/javascript/templates/test/dom_test1.html) 
```html
<style>
    body{
        padding:0;
        margin:0;
    }
    div{
        border:50px solid #1065e6;
        padding:50px;
        margin:50px;
    }
    #target{
        width:100px;
        height:2000px;
    }
</style>
    <div>
        <div id="target">
            Coding
        </div>
    </div>
 
<script>
var t = document.getElementById('target');
setInterval(function(){
    console.log('getBoundingClientRect : ', t.getBoundingClientRect().top, 'pageYOffset:', window.pageYOffset);
}, 1000)
</script>
```

> 오래된 브라우저에서는 pageYOffset 대신 scrollTop 속성을 사용해야 한다.

- 스크롤
    - 스크롤 변경을 위해 scrollLeft와 scrollTop 프로퍼티를 이용
    - [[실행]](https://idislbk.github.io/bklee1/javascript/templates/test/dom_test2.html) 
```html
<input type="button" id="scrollBtn" value="scroll(0, 1000)" />
<script>
    document.getElementById('scrollBtn').addEventListener('click', function(){
        window.scrollTo(0, 1000);
    })
</script>
```
- 스크린의 크기
    - 모니터의 크기 : screen.*
    - 뷰포트의 크기 : window.inner*
    ![](https://github.com/idislbk/bklee1/blob/master/javascript/img/viewportSize.PNG)

```html
<script>
console.log('window.innerWidth:', window.innerWidth, 'window.innerHeight:', window.innerHeight);
console.log('screen.width:', screen.width, 'screen.height:', screen.height);
</script>
```    
