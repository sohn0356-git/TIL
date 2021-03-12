import kr.multicampus.kotlin.insa.Staff
import kr.multicampus.kotlin.insa.Student
import kr.multicampus.kotlin.insa.Teacher

fun main(){
    var student:Student = Student("홍길동", "200201", 20)
    var teacher:Teacher = Teacher("이순신", "JAVA", 30)
    var staff:Staff = Staff("유관순", "교무과", 40)

    student.print()
    teacher.print()
    staff.print()
}
