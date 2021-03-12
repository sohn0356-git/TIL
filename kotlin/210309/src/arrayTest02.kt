fun main(){
    val myarr1 = intArrayOf(10,20,30,40,50)
    val myarr2 = myarr1.plus(60)
    println("myarr1 : ${myarr1.contentToString()}")
    println("myarr2 : ${myarr2.contentToString()}")
    println("myarr.first() : ${myarr1.first()}")
    println("myarr.contains(50) : ${myarr1.contains(50)}")
    println("30 in myarr1: ${30 in myarr1}")
    val myarr3 = arrayOf(50,100,98,77,23)
    println("myarr3 : ${myarr3.contentToString()}")
    val myarr4 = myarr3.sortedArray()
    println("myarr4 : ${myarr4.contentToString()}")
}