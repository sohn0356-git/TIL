
fun main(){
    var customer:Customer = Customer()
    var customer2:Customer = Customer(45,1011451)
}

class Customer{
    var age:Int = 0
    var telNum:Int = 0
    constructor(){
        println("매개변수가 없는 생성자")
    }
    constructor(age:Int, telNum:Int){
        this.age = age
        this.telNum = telNum
    }
    init{
        println("객체가 생성될 때 자동으로 실행되는 블럭")
    }
}

class Customer2 constructor(var age:Int, var telNum:Int){

}

class Customer3 (var age:Int, var telNum:Int){

}

class Customer4 (var age:Int, var name:String){
    var telNum:Int = 0
    constructor(age:Int, name:String, telNum:Int):this(age,name){
        this.telNum = telNum
    }
}