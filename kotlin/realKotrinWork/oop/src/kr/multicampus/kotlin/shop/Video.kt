import kr.multicampus.kotlin.shop.Content


class Video(title: String, var genre:String) : Content(title) {
    override fun totalPrice(){
        if(genre.equals("new")) {
            this.price = 2000
        } else if(genre.equals("comic")){
            this.price = 1500
        } else if(genre.equals("child")) {
            this.price = 1000
        } else{
            this.price = 500
        }
    }
}