# HTML



## 2일차



### CSS

* Cascading Style Sheets
  * 그라디언트
  * 그림자효과
  * 둥근모서리 사용가능
  * 멀티컬럼 레이아웃
  * 미디어 쿼리
  * 애니메이션 효과

　

* 적용 예

```html
<style>
h1 {
 color: red;
 /* This is a single-line comment */
 text-align: center;
}
</style>
<body>
 <h1>CSS TEST</h1>
</body>
```

　

* CSS를 적용하는 3가지 방법

  * External Style Sheet

  ```html
  <head>
  <link rel="stylesheet" type="text/css" href="mystyle.css">
  </head>
  ```

  　

  * Internal Style Sheet

  ```html
  <style>
  body {
   background-color: linen;
  }
  </style>
  ```

  　

  * Inline Style

  ```html
  <h1 style="color:blue;margin-left:30px;">This is a heading.</h1>
  ```

  　

* CSS Selector
  * Id는 전체 화면에 고유한 tag를 특정 id로 지정하여 사용
  * class는 다양한 tag에 동시에 스타일을 지정 할 때 사용
  * 여러 가지 tag를 그룹을 지어 스타일을 지정할 수 있다
  * 상위 하위로 나눠 특정 tag의 하위 tag만을 지정할 수 있다.
  * 다양한 기법을 통해 순서와 Not 조건을 이용할 수 있다.

　

* tag를 이용하는 방법

```html
p {
 text-align: center;
 color: red;
}
```



* Id를 이용하는 방법

```html
#para1 {
 text-align: center;
 color: red;
}
```



* class를 이용하는 방법

```html
.center {
 text-align: center;
 color: red;
}
```

　

* Attribute를 선택자로 설정

```html
<style>
    input[type=text]{
    color:red;
    }
    input[type=password]{
    color:blue;
    }
</style>
<body>
    <form>
        ID<input type="text" name="id"><br>
        PWD<input type="password" name="pwd"><br>
    </form>
</body>
```

　

* 마우스가 특정 tag를 선택 할 시 반응

| Selector |  Example  |       Description        |
| :------: | :-------: | :----------------------: |
| :active  | a:active  |   마우스로 클릭 할 시    |
|  :hover  |  a:hover  | 마우스로 tag를 선택할 시 |
| :visited | a:visited |   마우스로 click 이후    |



```html
a:active {
 background-color: blue;
}
a:hover {
 background-color: yellow;
}
a:visited {
 background-color: red;
}
```

　

* Table을 활용한 예시

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=\, initial-scale=1.0">
    <title>Document</title>
    <style>
        a{
            text-decoration:none;
            color:rgb(126, 19, 51);
        }
        ul, ol{
            list-style: none;
        }
        li > a:hover{
            color: cadetblue;
            background-color: darkgoldenrod;
        }
        table, th, td {
            border: 1px solid black;
        }
        table {
            width: 100%;
        }
        th {
            height: 70px;
            background-color: #4CAF50;
            color: white;
        }
        td {
            text-align: center;
        }
        td:hover {
            background-color: #f5f5f5;
        }

    </style>
</head>
<body>
    <h1>Test03</h1>
    <table>
        <thead>
            <tr><th>ID</th><th>PWD</th><th>NAME</th></tr>
        </thead>
        <tbody>
            <tr><td><a href="../test">Item01</a></td><td>pwd01</td><td>james01</td></tr>
            <tr><td><a href="../test2">Item02</a></td></tr>
            <tr><td><a href="..">Item03</a></td></tr>
            <tr><td><a href="..">Item04</a></td></tr>
            <tr><td><a href="{% url 'mycss:home' %}">Item05</a></td></tr>
            <tr><td><a href="">Item06</a></td></tr>
        </tbody>
    </table>
    <ul>
        
        
    </ul>
</body>
</html>
```

　

* 다수의 tag의 특정 위치를 지정

|      Selector      |                    ExampleD                     |                   Description                   |
| :----------------: | :---------------------------------------------: | :---------------------------------------------: |
|    :first-child    |                 li:first-child                  |            첫 번째 위치하는 tag 지정            |
|    :last-child     |                  li:last-child                  |           마지막에 위치하는 tag 지정            |
|   :nth-child(n)    |       li:nth-child(2n) li:nth-child(2n+1)       | 첫번째에서 짝수 또는 홀수 번째 위치한 tag 지정  |
| :nth-last-child(n) | ) li:nth-last-child(2n) li:nth-last-child(2n+1) | ) 마지막에서 짝수 또는 홀수번째 위치한 tag 지정 |



* 특정 위치의 문자 내용을 지정

|    Selector    |     Example     |           Description           |
| :------------: | :-------------: | :-----------------------------: |
| ::first-letter | p::first-letter | 특정 문장의 첫 번째 문자를 지정 |
|  ::first-line  |  p::first-line  | 특정 문장의 첫 번째 라인을 지정 |
|  ::selection   |  p::selection   |   마우스로 선택한 부분을 지정   |

　

* 기타 example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *{
            margin:0px;
            padding:0px;
        }
        a{
            text-decoration:none;
            color:black;
        }
        ul, ol{
            list-style:none;
        }
        header{
            width: 900px;
            height: 150px;
            background-color: black;
            color:white;
            text-align: center;
            line-height: 150px;
            font-size:1.5em;
            margin:0 auto;
        }
        nav{            
            margin:0 auto;
            width: 900px;
            height: 50px;
            line-height: 50px;
            border-bottom: 2px solid black;
        }
        nav > ul > li{
            margin: 0px 20px 0px 20px;
            float: left;
            display: block;
            border: 1px solid black;
            background: gray;
            color:white; 
        }
        nav > ul{
            width: 800px;
            margin:0 auto;
        }
        nav > ul > li > a{
            display:block;
            width: 100px;
            text-align: center;
        }
        nav > ul > li > a:hover{
            background-color: yellow;
        }
        section{
            width:900px;
            height:600px;
            background:red;
            margin:0 auto;
        }
        footer{
            width: 900px;
            height:30px;
            background:black;
            margin:0 auto;
        }
        
        aside{
            float: left;
        }

        #left_aside{
            width: 100px;
            height:600px;
            background-color: gray;
        }
        #center_aside{
            width: 700px;
            height:600px;
            background-color: white;
        }
        #right_aside{
            width: 100px;
            height:600px;
            background-color: pink;
        }

    </style>
</head>
<body>
    <h1>CSS 04</h1>
    <header>
        <h1>naver.com</h1>
    </header>
    <nav>
        <ul>
            <li><a href="#">HTML5</a></li>
            <li><a href="#">CSS3.0</a></li>
            <li><a href="#">JavaScript</a></li>
            <li><a href="#">jQuery</a></li>
            <li><a href="#">AJAX</a></li>
        </ul>
    </nav>
    <section>
        <aside id="left_aside"></aside>
        <aside id="center_aside"></aside>
        <aside id="right_aside"></aside>
    </section>
    <footer></footer>
    </body>
    
</html>
```

