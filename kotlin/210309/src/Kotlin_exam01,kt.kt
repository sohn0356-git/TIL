import java.util.*

fun main(){
    println("계산기\n1. 더하기\n2. 빼기\n3. 곱하기\n4.나누기")
    val key:Scanner = Scanner(System.`in`)
    println("원하는 작업을 선택하세요 : ")
    val option = key.nextInt()
    println("숫자1 : ")
    val num1 = key.nextInt()
    println("숫자2 : ")
    val num2 = key.nextInt()
    println(calc(num1,num2,option))
}

fun calc(num1:Int, num2:Int, op:Int): Int {
    when(op){
        1->{
            return num1+num2
        }
        2->{
            return num1-num2
        }
        3->{
            return num1*num2
        }
        4->{
            if(num2!=0)
            {
                return num1/num2
            }
            else
            {
                println("잘못된 입력");
                return 0
            }
        }
        else->{
            println("잘못된 입력");
            return 0
        }
    }

}