package kr.multicampus.kotlin.oop
/*
    var : variable
    val : value
 */
class Teacher(name:String,age:Int,val subject :String):Person(name,age) {
    override  fun print(){
        super.print();
        println("담당과목 : $subject ");
    }
}