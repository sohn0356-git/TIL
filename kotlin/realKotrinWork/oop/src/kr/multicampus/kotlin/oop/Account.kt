package kr.multicampus.kotlin.oop

class Account {
    var id:String = ""
    var amount:Int = 0
    constructor(id:String, amount:Int){
        this.id = id
        this.amount = amount
    }
    fun deposit(money:Int){
        amount += money
        inquiry()
    }
    fun withdraw(money:Int){
        if(amount>money) {
            amount -= money
            inquiry()
        } else {
            println("잔액이 부족합니다")
        }
    }
    fun inquiry(){
        println("잔액 : ${amount}")
    }
}