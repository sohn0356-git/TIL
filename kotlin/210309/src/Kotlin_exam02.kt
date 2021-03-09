import java.util.*

fun main(){
    val scanner: Scanner = Scanner(System.`in`)
    println("문자를 입력하세요 : ")
    val word:Char = scanner.next().single()
    println(display(word))
    println("숫자1 : ")
    val num1 = scanner.nextInt()
    println("숫자2 : ")
    val num2 = scanner.nextInt()
    printdata(num1,num2)
    val myarr = arrayOf(10,20,30,40,50)
    printSumArray(myarr)
}

fun display(word:Char):String{
    var ret:String = ""
    when(word){
        in '0'..'9'->{
            ret = "숫자입니다."
        }
        in 'a'..'z', in 'A'..'Z' ->{
            ret = "문자입니다."
        }
        else -> {
            ret = "판단할 수 없습니다."
        }
    }
    return ret
}

fun printdata(num1:Int, num2:Int){
    val range = IntRange(num1,num2)
    for(i in range){
        if(i%3==0)
        {
            print("${i} ")
        }
    }
    println()
}

fun printSumArray(myarr:Array<Int>){
    var sum = 0
    for(i in myarr){
        sum += i
    }
    println("sum : ${sum}")
}