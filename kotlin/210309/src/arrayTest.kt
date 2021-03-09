fun main(){
    val myarr1 = arrayOf(10,20,30,40,50)
    println(myarr1)
    for(i in myarr1){
        println(i)
    }
    println("=================")
    display(myarr1)
}

fun display(myarr:Array<Int>){
    println("display함수 => ${myarr.contentToString()}")
}