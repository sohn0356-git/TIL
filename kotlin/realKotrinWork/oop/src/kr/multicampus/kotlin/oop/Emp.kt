package kr.multicampus.kotlin.oop

class Emp {
    var name:String = ""
    var addr:String = ""
    var age:Int = 0

    constructor(name:String){
        this.name = name
        println("매개변수 1개 생성자")
    }

    constructor(name:String, addr:String):this(name){
        this.addr = addr
        println("매개변수 2개 생성자")
    }

    constructor(name:String, addr:String, age:Int):this(name,addr){
        this.age = age
        println("매개변수 3개 생성자")
    }
}