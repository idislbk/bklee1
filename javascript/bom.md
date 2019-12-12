# [JavaScript - Object Model](https://opentutorials.org/course/1375/6622)
-웹브라우저의 구성요소들은 하나하나가 객체화되어 있다. 자바스크립트로 이 객체를 제어해서 웹브라우저를 제어할 수 있게 된다.
 이 객체들은 서로 계층적인 관계로 구조화되어 있다

![](https://github.com/idislbk/bklee1/blob/master/javascript/img/objectModel.PNG)

## BOM - Browser Object Model
- 웹브라우저의 창이나 프래임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
- BOM은 전역객체인 Window의 프로퍼티와 메소드들을 통해서 제어함

## Window 객체
- Window 객체는 모든 객체가 소속된 객체이고, 전역객체이면서, 창이나 프레임을 의미
- 전역객체
    - Window 객체는 식별자 window를 통해서 얻을 수 있다. 또한 생략 가능
```
    alert('Hello world');
    window.alert('Hello world');
```

    - 전역변수와 함수가 사실은 window 객체의 프로퍼티와 메소드임
```
<!DOCTYPE html>
<html>
<script>
    var a = {id:1};
    alert(a.id);
    alert(window.a.id);
</script>
<body>
 
</body>
</html>
```

## 사용자와 커뮤니케이션 하기
- alert
- confirm
```
function func_confirm(){
                if(confirm('ok?')){
                    alert('ok');
                } else {
                    alert('cancel');
                }
            }
```
- prompt
```
if(prompt('id?') === 'egoing'){
                    alert('welcome');
                } else {
                    alert('fail');
                }
```

## Location 객체
- 현재 윈도우의 URL 알아내기
```
console.log(location.toString(), location.href);
```

## location 프로퍼티
```
console.log(location.protocol, location.host, location.port, location.pathname, location.search, location.hash)
```

## URL 변경하기
```
- location.href = 'http://egoing.net'; // 문서이동
- location = 'http://egoing.net'; // 문서이동
- location.reload();  // 현재 문서 리로드
```

## Navigator 객체
- 객체 프로퍼티 확인 방법
```
console.dir(navigator);
-appName
-appVersion
-userAgent
-platform
```

## 창제어

- [창제어](https://github.com/idislbk/bklee1/blob/master/javascript/templates/test/bom_test1.html)

- [새 창에 접근](https://github.com/idislbk/bklee1/blob/master/javascript/templates/test/bom_test2.html)

- [팝업차단](https://github.com/idislbk/bklee1/blob/master/javascript/templates/test/bom_test3.html)


















