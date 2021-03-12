package kr.multicampus.kotlin.oop

class Student (name:String,age:Int,var id:String):Person(name,age){
     override  fun print(){
         super.print();
        println("학 번 : $id ");
    }
}