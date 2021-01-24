# 운영체제 4일차

　

* 인터럽트(Interrupt)
  * 인터럽트 당한 시점의 레지스터와 program counter를 save한 후 CPU의 제어를 인터럽트 처리 루틴에 넘긴다.
  * Interrupt(하드웨어 인터럽트) : 하드웨어가 발생시킨 인터럽트
  * Trap(소프트웨어 인터럽트) 
    * Exception
    * System Call
  * 인터럽트 벡터
    * 해당 인터럽트의 처리 루틴 주소를 가지고 있음

　

* 시스템콜
  * 사용자 프로그램이 운영체제의 서비스를 받기 위해 커널 함수를 호출하는 것

　

* 동기식 입출력
  * I/O 요청 후 입출력 작업이 완료된 후에야 제어가 사용자 프로그램에 넘어감
* 비동기식 입출력
  * I/O가 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 사용자 프로그램에 즉시 넘어감

　

* DMA(Direct Memory Access)
  * 빠른 입출력 장치를 메모리에 가까운 속도로 처리하기 위해 사용
  * CPU의 중재 없이 device controller가 device의 buffer storage의 내용을 메모리에 block 단위로 직접 전송
  * 바이트 단위가 아니라 block 단위로 인터럽트를 발생시킴

　

* 함수
  * 사용자 정의함수
  * 라이브러리 함수
  * 커널 함수
    * 운영체제 프로그램의 함수

　

## 프로세스

* 프로세스의 개념
  * 프로세스의 문맥
    * CPU 수행 상태를 나타내는 하드웨어 문맥
  * 프로세스의 주소 공간
  * 프로세스 관련 커널 자료 구조
    * PCB, Kernel stack

　

* 프로세스의 상태
  * Running
    * CPU를 잡고 instruction을 수행중인 상태
  * Ready
    * CPU를 기다리는 상태
  * Blocked(wait, sleep)
    * CPU 를 주어도 당장 instruction을 수행할 수 없는 상태
    * Process 자신이 요청한 event가 즉시 만족되지 않아 이를 기다리는 상태

　

* PCB
  * 운영체제가 각 프로스세를 관리하기 위해 프로세스당 유지하는 정보
    * OS가 관리상 사용하는 정보
      * Process state, Process ID
      * scheduling information, priority
    * CPU 수행 관련 하드웨어 값
      * Program counter, Registers
    * 메모리 관련
      * Code, data, stack의 위치 정보
    * 파일 관련

　

* 문맥 교환(Context Switch)
  * CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정
    * CPU를 내어주는 프로세스의 상태를 그 프로세스의 PCB에 저장
    * CPU를 새롭게 얻는 프로세스의 상태를 PCB에서 읽어옴
  * System call이나 Interrupt 발생시 반드시 context switch가 일어나는 것은 아님