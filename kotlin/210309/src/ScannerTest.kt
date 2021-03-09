import java.util.*

fun main(){
    val key:Scanner = Scanner(System.`in`)
    val name:String = key.next()
    val age:Int = key.nextInt()
    key.nextLine()
    val info:String = key.nextLine()
    println("${name} ${age}")
    println("info:${info}")
}