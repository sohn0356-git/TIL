# JavaScript 공부

　

## 변수

　

### 자료형

* 기본타입(Primitive values)
  * Boolean
    * true, false
  * Null
  * Number
    * 모든 실수
  * String
    * 문자열
  * Symbol
    * 고유한 값

　

### 스코프

* 블럭

```javascript
let age = 37;

{
    age++;
	const name = 'Mark';
	console.log(name)
}
console.log(age);

//블럭 밖에서는 name 사용 불가
//age는 안밖에서 사용 가능
```

　

* var

```javascript
var a = 0;

(function(){
    a++;
    console.log(a);
}){};
console.log(a);

(function(){
    var b = 0;
    console.log(b);
})

//function 밖에서는 b 사용불가
```

　

## 호스팅

　

```javascript
function hello1(){
    console.log('hello1');
}

hello1();
hello2();

function hello2(){
    console.log('hello2');    
}

age = 6;
age++;
console.log(age);

var age;
```

* 아래 있는 선언(만)을 끌어 올린다.

　

## 함수

　

```javascript
function hello1(){
    console.log('hello1')
}
console.log(hello, typeof hello1);

function hello2(name){
    console.log('hello2', name)
}

function hello3(name){
	return `hello3 ${name}`
}
console.log(hello, typeof hello1);

const h1() = function(){
    console.log('hello1')
};

// new Function('인자1','인자2',..., 함수의 바디 );

const hello = (name,age) => {
    console.log('hello',name,age);
};
```

　

### HTML 연동(code sandbox)

```javascript
const increase = document.getElementById("increase");
const decrease = document.getElementById("decrease");
const buttons = document.querySelectorAll("button");
increase.onclick = () => {
    const current = parseInt(number.innerText, 10);
    console.log('increase가 선택됨');
}
decrease.onclick = () => {
    console.log('decrease가 선택됨');
}

//모달
const open = document.getElementById("open");
const close = document.getElementById("close");
const modal = document.querySelector(".modal-wrapper");

open.onclick = () => {
    modal.style.display = "flex";
}

close.onclick = () => {
    modal.style.display = "none";
}

```

