# db Project



## 개요

* `Python`에 있는 `sqlite3` package를 이용하여 db프로젝트를 진행해보았다.
* 팀원 : 김현수, 손경주, 한상범, 한재영
* 과일가게에 상품을 주문하는 고객에 초점을 맞추어서 작성했다.
* 추후에 사용자로부터 새로운 테이블을 생성할 수 있는 기능의 추가 또한 고려 중이다.



## 구성요소

* dbUtil.py
  * FruitDB Class
    * Class 변수
      * db와 연결을 위한 **con**과 **cursor**
      * db의 table이름을 저장하는 **tableName**
      * db의 컬럼 정보를 저장하는 **dbList**
      * db의 컬럼 정보중 int 속성의 컬럼 정보를 저장하는 **dbListInt**
      
       　
      
    * 맴버 함수
      * Constructor        
        
        * 사용자로부터 원하는 정보를 받아 저장하는 dict 맴버 변수 __data
      * insert        
        
        * 사용자로부터 받은 정보를 table에 넣는 함수
      * query        
        
        * 사용자로부터 받은 질의를 만족하는 데이터를 table에서 찾아서 출력
      * update        
        * 사용자로부터 받은 수정사항을 데이터에 적용시키는 함수
        
        　 
      
    * Class 함수
      * connectDB
        * `order.db`와 연결하는 함수
      * makeTable
          * `fruits`테이블이 생성되어있지 않을 경우 생성해주는 함수
      * select
        * 사용자로부터 입력 받은 정보에 맞는 데이터를 table에서 찾아서 출력
      * delete
        * 사용자로부터 입력 받은 `id`를 key로 갖는 데이터를 table에서 찾아서 삭제
      * closeDB
        * db와의 연결을 해제

 　

* dbApp.py
  * db와 연결을 한 뒤 사용자에게 Menu를 선택하게 한다.
  * Menu
    * c (create) : 사용자로부터 새로운 데이터를 추가한다.
    * r (readAll) : 테이블에 있는 모든 데이터를 읽어온다.
    * ro : 과일 이름을 입력받고 해당하는 데이터를 읽어온다.
    * rc (readCondition) : 조건을 입력받고 해당하는 데이터를 읽어온다.
    * u (update) : 수정하고 싶은 데이터를 입력받고 데이터를 수정한다.
    * d (delete) : `id`를 입력받고 해당하는 데이터를 제거한다.
    * q (quit) : db와 연결을 해제하고 프로그램을 종료한다.

 　

* order.db

  * fruits

    ```
      id CHAR(16) PRIMARY KEY,
      name CHAR(16),
      qt NUMBER(5),
      price NUMBER(10),
      grade CHAR(15),
      origin CHAR(20)
    ```

