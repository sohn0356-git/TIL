package kr.multicampus.kotlin.oop

fun main(){
    var child:Child = Child()
    child.show()
    child.display()
}

open abstract class Parent{
    fun display(){
        println("parent의 일반메소드")
    }
    //추상메소드
    open abstract fun show()
}

class Child:Parent(){
    override fun show(){
        println("child의 상속메소드")
    }
}