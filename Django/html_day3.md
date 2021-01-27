# HTML



## 3일차



### JavaScript

* HTML 내부 Content를 자유롭게 변경 추가가 가능하게 한다.
* CSS를 자유롭게 변경한다.
* Event 처리 및 Validation
* Web Page에서의 프로그램 부분을 담당한다.

　

#### JavaScript의 위치

* JavaScript in head

```html
<!DOCTYPE html>
<html>
    <head>
        <script>
        function myFunction() {
        document.getElementById("demo").innerHTML =
        "Paragraph changed.";
        }
    </script>
    </head>
    <body>
        <h1>My Web Page</h1>
        <p id="demo">A Paragraph</p>
        <button type="button" onclick="myFunction()">Try it</button>
    </body>
</html>
```

　

* JavaScript in body

```html
<!DOCTYPE html>
    <html>
    <body>
        <h1>My Web Page</h1>
        <p id="demo">A Paragraph</p>
        <button type="button" onclick="myFunction()">Try it</button>
        <script>
            function myFunction() {
            document.getElementById("demo").innerHTML = "Paragraph changed.";
            }
        </script>
    </body>
</html>
```

　

* External JavaScript

```html
function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}
```

　

#### Data Type & Function

* 변수 선언
  * 문자, 숫자, _, $ 기호를 포함할 수 있다.
  * 스페이스는 포함할 수 없다.
  * 반드시 문자 또는 _, $로 시작해야 하며 숫자로 시작할 수 는 없다.
  * 문자는 대소문자를 구분한다.
  * 예약어는 사용할 수 없다.

```html
<script>
        var data1 = 100;
        // var 1data = 200;
        var $data = 300;
        // var data one = 400;
        var data = 500;
        var DATA = 600;
</script>
```



* 변수 타입
  * undefined : 어떠한 데이터 타입도 선언되지 않은 상태
  * number : 실수, 정수 모두 포함
  * boolean : true, false를 의미함
  * string : 문자열, character 모두 포함
  * array : 배열
  * object : 객체 type을 의미
  * function : 함수를 의미


　

* 기타 example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script>
        function a(d1){
            alert('a ...'+d1);
        }
        var b = function(d2){
            alert('b ...'+d2);
        };
        function c(d1){
            var result = d1*1000;
            return result;
        }
        // a(100);
        // b('abc');
        // var t = c(50);
        // alert(t);
        var f1 = function(){
            return 10;
        };

        function f2(f){
            return f();
        }

        var res = f2(f1);
        
        var f3 = function(){
            return function(){
                return 50;
            };
        };

        // alert(f3()());
        var str1 = "alert('abc')";
        // eval(str1);

        var str2 = '{"id":"id01","age":30}'
        // var json = eval(str2);
        var str3 = '{"id":"id01","age":30,"score":[90,80,90,100]}'
        var o = JSON.parse(str3);
        console.log(o.score);
        
        var a = 10;
        if(a > 100){
            alert('big number');
        }
        else{
            alert('small number');
        }

    </script>
</head>
<body>
    
</body>
</html>
```

