package kr.multicampus.kotlin.oop

open class Person(var name:String,var age:Int) {
    open fun print(){
        print("성 명 :$name 나 이 : $age   ");
    }
}