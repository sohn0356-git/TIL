package kr.multicampus.kotlin.insa

class Staff {
    var name:String = ""
    var dept:String = ""
    var age:Int = 0

    constructor(name:String){
        this.name = name
    }

    constructor(name:String, dept:String):this(name){
        this.dept = dept
    }

    constructor(name:String, dept:String, age:Int):this(name,dept){
        this.age = age
    }

    fun print(){
        println("이 름 : ${name} 나 이 : ${age} 부 서 : ${dept}")
    }
}