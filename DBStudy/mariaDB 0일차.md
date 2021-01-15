# MariaDB

## 0일차

* 오늘부터 MariaDB를 학습해보겠다.
* 교재는 [이것이 MariaDB다](https://www.hanbit.co.kr/store/books/look.php?p_code=B1764282969)를 참고해서 진행하겠다.
* 학습을 위해 먼저 [설치](https://downloads.mariadb.org/interstitial/mariadb-10.3.11/winx64-packages/mariadb-10.3.11-winx64.msi/from/https%3A//archive.mariadb.org/)를 해보자.

　

![mariadb_0일차_01](md-images/mariadb_0%EC%9D%BC%EC%B0%A8_01.JPG)
* 설치를 할 때에는 default설정으로 하면 된다. 단, `password`는 잘 기억하자!
* 설치가 끝났으면 HeidiSQL이라는 프로그램이 생겼을 것이다. 실행해보자!

　


![mariadb_0일차_02](md-images/mariadb_0%EC%9D%BC%EC%B0%A8_02.JPG)

* 신규를 눌러서 새로운 세션을 만들어보자.
* 이 때 암호는 설치중에 설정했던 암호이다.

　

![mariadb_0일차_03](md-images/mariadb_0%EC%9D%BC%EC%B0%A8_03.JPG)

* 이제 이 곳에서 열심히 작업하면 된다.
* SQL문을 테스트해보기 위해서 Sample Data를 [이 곳](https://github.com/datacharmer/test_db)에서 다운받을 수 있다.
* 끝으로 환경변수를 설정하며 마무리한다.

　

![mariadb_0일차_04](md-images/mariadb_0%EC%9D%BC%EC%B0%A8_04.JPG)

* SETX PATH "C:\Program Files\MariaDB 10.3\bin;%PATH%" /M
