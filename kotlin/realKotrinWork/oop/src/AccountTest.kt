import kr.multicampus.kotlin.oop.Account
import java.util.*

fun main(){
    var account:Account = Account("111-222-333", 1000000)
    var scanner:Scanner = Scanner(System.`in`)
    var amount:Int = 0
    var menu:Int = 0
    while(true){
        println("1. 입금하기")
        println("2. 출금하기")
        println("3. 잔액조회")
        menu = scanner.nextInt()

        when(menu){
            1-> {
                print("입금할 금액을 입력하세요 : ")
                amount = scanner.nextInt()
                account.deposit(amount)
            }
            2->{
                print("입금할 금액을 입력하세요 : ")
                amount = scanner.nextInt()
                account.withdraw(amount)
            }
            3->{
                account.inquiry()
            }
            else ->{
                println("다시 입력하세요")
            }
        }
    }
}