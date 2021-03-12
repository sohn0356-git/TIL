package kr.multicampus.kotlin.shop

abstract class Content(var title:String) {
    var price:Int = 0
    open abstract fun totalPrice()
    fun show(){
        println("${title}의 가격은 ${price}원입니다.")
    }
}