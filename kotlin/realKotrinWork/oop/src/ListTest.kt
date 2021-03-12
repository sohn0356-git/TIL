fun main(){
    val list1 = listOf(1,2,4,10,5)
    println(list1)
    var list2 = mutableListOf<Int>(1,2,4,10,5)
    list2[0]=10
    list2.add(20)
    println(list2)
    var set1 = setOf<Int>(1,6,2,3,7,4,5,1)
    println(set1)
    var map1 = mapOf<Int,Int>(1 to 1, 3 to 2, 2 to 4)
    println(map1)
}