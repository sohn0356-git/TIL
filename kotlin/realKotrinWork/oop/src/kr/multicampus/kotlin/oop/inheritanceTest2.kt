package kr.multicampus.kotlin.oop
//*********************상속연습**************************************
fun main() {
    val obj1:SubClass = SubClass();
    println("obj1(SubClass)객체로 부모 클래스의 멤버변수 접근:${obj1.superVal}")
    obj1.display()

    val obj2:SubClass2 = SubClass2();
    println("obj2(SubClass2)객체로 부모 클래스의 멤버변수 접근:${obj2.superVal}")
    obj2.display()
}
//class를 정의하면 코틀린이 컴파일되고 자바코드로 변환되면서 public final이 추가
/*
   final의 의미
   변수: 상수
   메소드: 재정의할 수 없는 메소드
   클래스: 상속할 수 없는 클래스
 */
//상위클래스는 open을 이용해서 상속이 가능한 클래스로 만들어야 한다.
open class SuperClass{
    var superVal = 100;
    fun display(){
        println("부모클래스의 display");
    }
}
//클래스를 상속하는 경우 반드시 상위클래스의 생성자를 호출해야 한다.\
//상위클래스의 주 생성자를 주로 호출한다.
//상위클래스에 생성자가 정의되어 있지 않으면 매개변수가 없는 생성자를 호출한다.
class SubClass:SuperClass(){

}
class SubClass2:SuperClass{
    constructor():super(){//SubClass2의 객체가 생성되면 부모의 매개변수없는 생성자를 먼저 호출한다.

    }
}



