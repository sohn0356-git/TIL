package kr.multicampus.kotlin.insa

class Student {
    var name:String = ""
    var id:String = ""
    var age:Int = 0

    constructor(name:String, id:String, age:Int){
        this.name = name
        this.id = id
        this.age = age
    }

    fun print(){
        println("이 름 : ${name} 나 이 : ${age} 학 번 : ${id}")
    }
}