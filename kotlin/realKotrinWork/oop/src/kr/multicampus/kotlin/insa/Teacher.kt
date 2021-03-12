package kr.multicampus.kotlin.insa

class Teacher(var name:String, var subject:String, var age:Int) {
    fun print(){
        println("이 름 : ${name} 나 이 : ${age} 담당과목 : ${subject}")
    }
}