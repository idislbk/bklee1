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
    >> [Test Url](http://localhost:5000/test/text_test2.html) : http://localhost:5000/test/text_test2.html 

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
> 예제
>>    [샘플소스](https://github.com/idislbk/bklee1/blob/master/javascript/templates/test/text_test3.html)
    <br/>
    [Test Url](http://localhost:5000/test/text_test3.html) : http://localhost:5000/test/text_test3.html 
    <br/>
>>    [중첩 예제소스](https://github.com/idislbk/bklee1/blob/master/javascript/templates/test/text_test4.html)
    <br/>
    [Test Url](http://localhost:5000/test/text_test4.html) : http://localhost:5000/test/text_test4.html 
