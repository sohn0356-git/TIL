# 운영체제 5일차

　

## 프로세스

　

### 스케줄러

* Long-term scheduler(Job scheduler)
  * 시작 프로세스 중 어떤 것들을 ready queue로 보낼지 결중
  * 프로세스에 memory(및 각종 자원)을 주는 문제
  * time sharing system에는 보통 장기 스케줄러가 없음(무조건 ready)

　

* Short-term scheduler(CPU scheduler)
  
  * 어떤 프로세스를 다음번에 running 시킬지 결정
  * 충분히 빨라야 함(millisecond)
  
  
  
* Medium-term scheduler(Swapper)

  * 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄
  * 프로세스에게서 memory를 뺏는 문제

　

### 프로세스의 상태

　

* Running
  * CPU를 잡고 instruction을 수행중인 상태
* Ready
  * CPU를 기다리는 상태
* Blocked(wait, sleep)
  * CPU 를 주어도 당장 instruction을 수행할 수 없는 상태
  * Process 자신이 요청한 event가 즉시 만족되지 않아 이를 기다리는 상태

* Suspended(stopped)
  * 외부적인 이유로 프로세스의 수행이 정지된 상태
  * ex) 사용자가 프로그램을 정지시킨 경우

　

* 문맥 교환(Context Switch)
  * CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정
    * CPU를 내어주는 프로세스의 상태를 그 프로세스의 PCB에 저장
    * CPU를 새롭게 얻는 프로세스의 상태를 PCB에서 읽어옴
  * System call이나 Interrupt 발생시 반드시 context switch가 일어나는 것은 아님

　

* 프로세스 생성
  * 부모 프로세스가 자식 프로세스 생성
  * 프로세스의 트리(계층 구조) 형성

　

## Thread

* A thread is a basic unit of CPU utilization

　

* Thread의 구성
  * program counter
  * register set
  * stack space

　

* Thread의 장점

  * 다중 스레드로 구성된 태스크 구조에서는 하나의 서버 스레드가 blocked(waiting) 상태인 동안에도

    동일한 태스크 내의 다른 스레드가 실행(running) 되어 빠른 처리를 할 수 있다.

  * 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughput)과 성능 향상을 얻을 수 있다.

  * 스레드를 사용하면 병렬성을 높일 수 있다.



