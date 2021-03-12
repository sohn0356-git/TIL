fun main(){
    var a = 5
    var myarr = arrayOfNulls<Super>(a)
    myarr[0] = SubA()
    myarr[1] = SubA()
    myarr[2] = SubB()
    for(element in myarr){
        println("element : ${element}")
    }
    println("${myarr[0]?.s}")

    var subA = SubA()
    println("${subA.a}")

}

open class Super{
    val s = 1
}

class SubA:Super(){
    val a = 5
}

class SubB:Super(){
    val b = 6
}