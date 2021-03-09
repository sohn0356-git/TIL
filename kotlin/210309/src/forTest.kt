fun main(){
    val numRange = 1..10 step 2
    for(i in numRange){
        println(i)
    }

    val numRange2 = 100 downTo 1 step 2
    for(i in numRange2){
        println(i)
    }
}