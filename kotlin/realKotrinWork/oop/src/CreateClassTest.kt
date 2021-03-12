fun main(){
    var myClass:MyClass2 = MyClass2("abc",5)
    myClass.print()

}

class MyClass2{
    var name:String = ""
    var age:Int = 0
    constructor(name:String, age:Int){
        this.name=name
        this.age=age
    }
    fun print(){
        println("${name} and ${age}")
    }
}
