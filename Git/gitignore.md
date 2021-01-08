#  gitignore

* `git`으로 관리하지 않을 파일을 관리

`.gitignore`라는 파일을 만들어서 디렉토리를 관리한다.

```bash
a.txt # 특정 파일
venv/ # 특정 폴더
*.csv # 특정 확장자
```



* 일반적으로 로컬 개발환경과 관련도니 파일/폴더는 git으로 관리하지 않는다.
  * ex) 운영체제(윈도우/Mac), IDE/Texteditor, 특정 언어에서 실행시 생성되는 파일
  * 아래의 사이트를 참고하여 gitignore파일을 만들 수 있다.
    * https://gitignore.io
* 추가적인 파일(고객 데이터, key값 등)도 등록할 수 있다.