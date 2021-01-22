# 운영체제 3일차

　

* 운영체제란?

  * 컴퓨터 하드웨어 바로 위에 설치되어 사용자 및 다른 모든 소프트웨어와

    하드웨어를 연결하는 소프트웨어 계층

  * 컴퓨터 시스템을 편리하게 사용할 수 있는 환경을 제공

  * 컴퓨터 시스템의 자원을 효율적으로 관리

　

* 운영체제의 분류
  * 단일 작업
    * ex) MS-DOS 프롬프트 상에서는 한 명령의 수행을 끝내기 전에 다른 명령을 수행시킬 수 없음
  * 다중 작업
    * ex) UNIX, MS Windows 등에서는 한 명령의 수행이 끝나기 전에 다른 명령이나 프로그램을 수행할 수 있음
  * 단일 사용자
    * ex) MS-DOS, MS Windows
  * 다중 사용자
    * ex) UNIX, NT server
  * 일괄 처리 => 작업 요청을 일정량 모아서 한꺼번에 처리
    * ex) 초기 Punch Card 처리 시스템
  * 시분할
    * ex) UNIX
  * 실시간 => 정해진 시간 안에 어떠한 일이 반드시 종료됨이 보장되어야 하는 OS
    * ex) 원자로/공장 제어, 미사일 제어

　

> 용어
>
> * Multitasking
> * Multiprogramming
> * Time sharing
> * Multiprocess
>
> 
>
> 위의 용어들은 컴퓨터에서 여러 작업을 동시에 수행하는 것을 뜻한다.
>
> Multiprogramming은 여러 프로그램이 메모리에 올라가 있음을 강조
>
> Time sharing은 CPU의 시간을 분할하여 나누어 쓴다는 의미를 강조
>
> ---
>
> Multiprocessor : 하나의 컴퓨터에 CPU가 여러 개 붙어 있음을 의미

 　

* Mode bit
  * 사용자 프로그램의 잘못된 수행으로 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기 위한 보호 장치 필요
  * 0 : 모니터 모드 - OS 코드 수행(Interrupt Or Exception)
  * 1 : 사용자 모드 - 사용자 프로그램 수행
* Timer
  * 정해진 시간이 흐른 뒤 운영체제에게 제어권이 넘어가도록 인터럽트 발생
  * Time sharing을 구현하기 위해 널리 이용됨