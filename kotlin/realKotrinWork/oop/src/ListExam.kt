fun main(){
    var l1 = mutableListOf<Int>()
    var l2 = mutableListOf<Boolean>()
    for(i in 1..10){
        l1.add(i)
    }
    for(e in l1){
        if(e%2==0){
            l2.add(true)
        }else{
            l2.add(false)
        }
    }
    println(l1)
    println(l2)

    var myarr = intArrayOf(10,20,30,40,50)
    var l = toList(myarr)
    var m = toMap(myarr)

    println(l)
    println(m)
}

fun toList(arr:IntArray):List<Int>{
    var l = mutableListOf<Int>()
    for(e in arr){
        l.add(e)
    }
    return l
}

fun toMap(arr:IntArray):Map<Int, Int>{
    var m = mutableMapOf<Int, Int>()
    for(e in arr){
        m.put(e+10, e)
    }
    return m
}