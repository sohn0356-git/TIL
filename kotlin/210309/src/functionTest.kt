fun main(){
    // Unit - void와 동일
    test()
    test2()
    println("${add(1,2)}")
    println("${add(num2=30)}")
    display()
    var a = display(10)
    println(a)
    outerFunc()
    innerFunc()
}

fun test(){
    println("test함수")
    println("--------------------")
}

fun test2():Unit{
    println("test함수")
    println("--------------------")
}

fun add(num1:Int=10, num2:Int=20):Int{
    return num1 + num2
}

fun display():Unit{
    println("display - 매개변수 없는 함수")
}

fun display(num:Int):Int{
    println("display - 매개변수 1개인 함수")
    return num*10
}

fun display(num1:Int=20, num2:Int=20):Int{
    println("display - 매개변수 2개인 함수")
    return num1*10+num2
}

fun innerFunc(){
    println("Inner func")
}
fun outerFunc(){
    println("outerFunc")
    fun innerFunc(){
        println("outerFunc의 innerfunc")
    }
    innerFunc()
    println("----------------------------------")
}