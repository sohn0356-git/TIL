package exam

fun main(){
    println("Hello")
    val num1:Int = 100
    val num2:Int = 200
    val result:Int = num1+num2
    println("num1:${num1}, num2:${num2}를 더한 결과 : ${result}")
    val result2 = num1+num2
    println("result2:${result2}")

    //val과 var의 차이
    val num3:Int = 100
    var num4:Int = 200

//    num3 = 200    //재설정 불가
    num4 = 200
    var num5:Int ?= null    // null을 허용하는 변수
    var num6:Int = 200
    num5 = num6
    num6 = 50
    println("${num5} ${num6}")
    var num7:Int = num5
}