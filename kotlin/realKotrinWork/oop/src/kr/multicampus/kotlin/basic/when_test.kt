fun main() {
    /*
        when switch문과 비슷
        1. 형식
           when(변수 or 연산식){  -> 변수나 연산식으로 평가
                값1 -> 실행할 코드
                값2 -> 실행할 코드
                값3 -> 실행할 코드
                값4 -> 실행할 코드
                  ......
                else -> 정의한 값을 만족하지 않는 경우 
           }
     */
    //when의 일반적인 문법
    val code = 2;
    when(code){
        1 -> println("입력에 관련된 작업을 수행");
        2 ->{
            println("출력에 관련된 작업을 수행");
            println("비밀번호입력");
        }
        3 -> println("조회에 관련된 작업을 수행");
        else -> println("값 잘못 입력");
    }
    println("*************************************************");
    val code2 = 5;
    //case 여러 개를 같이 평가
    when(code2){
        1,2 -> println("입력에 관련된 작업을 수행");
        3,4 ->{
            println("출력에 관련된 작업을 수행");
            println("비밀번호입력");
        }
        5,6 -> println("조회에 관련된 작업을 수행");
        else -> println("값 잘못 입력");
    }
    println("*************************************************");
    val code3 = 0.3;
    //case 여러 개를 같이 평가
    when(code3){
        0.1 -> println("입력에 관련된 작업을 수행");
        0.2 ->{
            println("출력에 관련된 작업을 수행");
            println("비밀번호입력");
        }
        0.3 -> println("조회에 관련된 작업을 수행");
        else -> println("값 잘못 입력");
    }
    println("*************************************************");
    val code4 = "a01";
    //case 여러 개를 같이 평가
    when(code4){
        "a01"  -> println("a01");
        "a02" ->{
            println("a02");
            println("a02");
        }
        "a03" -> println("a03");
        else -> println("else");
    }
    println("*************************************************");
    val code5 = 10;
    //case 여러 개를 같이 평가
    when(code5){
        in 1..9  -> println("1부터 9사이값");
        in 10..19 ->{
            println("10부터 19사이값");
        }
        in 20..29 -> println("20부터 29사이값");
        else -> println("else");
    }
    val myresult1 = setValue(90);
    val myresult2 = setValue(80);
    val myresult3 = setValue(70);
    println("myresult1=$myresult1");
    println("myresult2=$myresult2");
    println("myresult3=$myresult3");
}
//
fun setValue(num:Int) = when(num){
    90 -> "합격";
    80 -> "보류";
    70 -> "불합격";
    else -> "else";
}