# HTML



## 1일차



### HTML

* HTML(Hyper Text Markup Language)

```html
<!DOCTYPE html>
<!-- DOCTYPE 문서 유형 지정 -->
<html>
    <head>
        <meta charset="EUC-KR">
        <title>Insert title here</title>
        
        <!-- CSS style 영역
			전체 화면의 Style 지정-->
        <style>
        </style>
        
        <!-- JavaScript 영역
        	 Program 영역 -->
        <script>
        </script>
        
    </head>
    
    <!-- 화면에 표현되어지는 내용 -->
    <body>        
    </body>
</html>
```

　

### META

```html
<meta name="keywords" content="HTML, CSS, JavaScript">
<!-- 검색 엔진 키워드를 정의합니다. -->

<meta name="description" content="HTML and CSS">
<!-- 웹 페이지에 대한 설명을 정의 -->

<meta name="author" content="Hege Refsnes">
<!-- 페이지의 저자를 정의 -->

<meta http-equiv="refresh" content="30">
<!-- 새로 고침 문서 30초마다 -->

<meta charset="EUR-KR">
<!-- 언어 설정 -->
```

　

### STYLE

* STYLE영역은 HTML5의 문서에서 화면의 디자인을 적용하는 역할을 담당한다.
* CSS를 이용하여 각 tag에 스타일을 적용한다.

　

```html
<style>
    ul{
        margin : 0px;
        padding : 0px;
    }
    li{
        border:1px solid blue;
        text-align : center;
        margin : 0px;
        padding : 0.53m;
    }
</style>
```

　

### SCRIPT

* SCRIPT 영역은 HTML5의 문서에서 프로그램 부분과 다양한 API를 적용하는 역할을 담당한다.
* JavaScript를 이용하여 프로그램을 작성하며 jQuery나 기타 다양한 Script언어를 사용한다.

　

```html
<script>
var data = [{'id':'id01','name':'이말숙'},
            {'id':'id02','name':'김말숙'}];
for(var i in data){
    with(data[i]){
        alert(id+''+name);
    }
}
</script>
```



* HTML 예졔

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Register</h1>
    <form>
        <fieldset>
            <legend>Register Page</legend>
            <input type="color" name="favcolor">
            <input type="date" name="regdate">
            <input type="range" name="points" min="0" max="10"><br/>
            <label for="id">ID</label>
            <input type="text" name="rid" id="id"><br/>
            <label for="pwd">PWD</label>
            <input type="password" name="rpwd" id="pwd"><br/>
            <label for="age">ID</label>
            <input type="number" name="rage" id="age"><br/>
            <p>직업</p>
            <label for="job1">선생</label>
            <input type="radio" name="r1" value="cr1" id="job1">
            <label for="job2">교장</label>
            <input type="radio" name="r1" value="cr2" id="job2">
            <label for="job3">학생</label>
            <input type="radio" name="r1" value="cr3" id="job3">
            <p>취미</p>
            <label for="h1">공부</label>
            <input type="checkbox" name="c1" value="ch1" id="h1">
            <label for="h2">운동</label>
            <input type="checkbox" name="c1" value="ch2" id="h2">
            <label for="h3">독서</label>
            <input type="checkbox" name="c1" value="ch3" id="h3">
            <p>자기소개</p>
            <textarea rows="10" cols="50" name="tt"></textarea>
            <p>전화번호</p>
            <select name="p">
                <option value="skt">SKT</option>
                <option value="kt">KT</option>
                <option value="lgt">LGT</option>
            </select>
            <br/>
            <input type="submit" value="Register">
            <inut type="reset" value="Reset">/input>
        </fieldset>
    </form>
</body>
</html>
```

