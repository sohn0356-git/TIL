import kr.multicampus.kotlin.shop.Book
import kr.multicampus.kotlin.shop.Content

fun main() {
    var contents = arrayOfNulls<Content>(5)
    contents[0] = Video("변호인", "new")
    contents[1] = Video("탐정", "comic")
    contents[2] = Video("헬로카봇", "child")
    contents[3] = Book("감자(책)", 1990)
    contents[4] = Video("뽀로로", "horror")
    for (elem in contents) {
        if (elem != null) {
            elem.totalPrice()
            elem.show()
        }
    }
}