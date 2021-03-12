import java.util.Scanner

fun main() {
    val key:Scanner = Scanner(System.`in`);
    println("결과:${display('a')}");
    println("결과:${display('F')}");
    println("결과:${display('7')}");
    println("결과:${display('#')}");
    println("결과:${10/3.toDouble()}");
    print("숫자1:");
    val num1:Int = key.nextInt();
    print("숫자1:");
    val num2:Int = key.nextInt();
    printdata(num1..num2);
    val myarr = arrayOf(100,90,90,80,97);
    printSumArray(myarr);
}
fun printSumArray(myarr:Array<Int>){
    var sum = 0;
    var avg =  0.0;
    var count = 0;
    for(i in myarr){
        sum = sum + i;
        count++;
    }
    println("합계:$sum");
    println("평균:${sum/count.toDouble()}");
}
fun display(data:Char) = when(data){
    in '0'..'9' -> "숫자입니다.";
    in 'a'..'z', in 'A'..'Z' -> "문자입니다.";
    else  -> "판단할 수 없습니다.";
}
fun printdata(data:IntRange){
    for(i in data){
        if(i%3==0){
            println("값:$i");
        }
    }
}

