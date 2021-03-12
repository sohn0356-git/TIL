package kr.multicampus.kotlin.bank
/*
1) 입금하기
    : 입력받은 금액을 내 잔액에 더해주기
2) 출금하기
    : 입력받은 금액을 내 잔액에서 빼주기
      금액이 내 잔액보다 작은 경우에만 작업하기
3) 잔액조회하기
    : 현재 잔액을 조회하기
 */
class Account{
    var accId:String="";
    var balance:Int=0;
    constructor(accId:String,balance:Int){
        this.accId = accId;
        this.balance = balance;
    }
    fun deposit(money:Int){
        balance = balance + money;
    }
    fun withdraw(money:Int){
        if(balance>=money){
            balance = balance - money;
        }else {
            println("출금할 수 없습니다.");
        }
    }
    fun print(){
        println("잔액:$balance");
    }
}