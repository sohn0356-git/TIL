fun main(){
    val num1 = 100
    var code = 5
    when(code) {
        1, 5 -> {
            println("Insertion")
        }
        2 -> {
            println("Search")
        }
        3 -> {
            println("Deletion")
        }
        else -> {
            println("Ohters")
        }
    }

    var code2 = "A04"
    when(code2) {
        "A01", "A02" -> {
            println("Insertion")
        }
        "A03" -> {
            println("Search")
        }
        "A04" -> {
            println("Deletion")
        }
        else -> {
            println("Ohters")
        }
    }

    var code3 = 10
    when(code3) {
        in 1..9 -> {
            println("Insertion")
        }
        in 10..19 -> {
            println("Search")
        }
        in 20..30 -> {
            println("Deletion")
        }
        else -> {
            println("Ohters")
        }
    }
    val a = setValue(20)
    println(a)
}

fun setValue(num:Int) = when(num){
    90->"합격"
    80->"보류"
    70->"불합격"
    else -> "재입력"
}