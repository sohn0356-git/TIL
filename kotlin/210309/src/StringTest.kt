fun main(){
    val str = "hello"
    println("str[0] = ${str[0]}")
    val str2 = "Python Android C Java Kotlin"
    var strdata = str2.split(" ")
    println("strdata[1] : ${strdata[1]}")

    var sb1 = StringBuffer()
    sb1.append("java")
    sb1.append("kotlin")
    sb1.append("android")
    sb1.append("python")
    println("sb1 : ${sb1}")
}