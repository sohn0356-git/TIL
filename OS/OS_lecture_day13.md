# 운영체제 13일차

　

## Deadlock(6-3~6-3)

　

### Deadlock 발생의 4가지 조건

* Mutual exclusion
  * 매 순간 하나의 프로세스만이 자원을 사용할 수 있음
* No preemption
  * 프로세스는 자원을 스스로 내어놓을 뿐 강제로 빼앗기지 않음
* Hold and wait
  * 자원을 가진 프로세스가 다른 자원을 기다릴 때 보유 자원을 놓지 않고 계속 가지고 있음
* Circular wait
  * 자원을 기다리는 프로세스 간에 사이클이 형성되어야 함

　

### Resource-Allocation Graph

* 그래프에 cycle이 없으면 deadlock이 아니다
* 그래프에 cycle이 있으면
  * if only one instance per resource type, then deadlock
  * if several instances per resource type, possibility of deadlock

　

### Deadlock의 처리방법

* Deadlock Prevention
  * 자원 할당 시 Deadlock의 4가지 필요 조건 중 어느 하나가 만족되지 않도록 하는 것
* Deadlock Avoidance
  * 자원 요청에 대한 부가적인 정보를 이용해서 deadlock의 가능성이 없는 경우에만 자원을 할당
  * 시스템 state가 원래 state로 돌아올 수 있는 경우에만 자원 할당
* Deadlock Detection and recovery
  * Deadlock 발생은 허용하되 그에 대한 detection 루틴을 두어 deadlock 발견시 recover
* Deadlock Ignorance
  * Deadlock을 시스템이 책임지지 않음
  * UNIX를 포함한 대부분의 OS가 채택

　

### Deadlock Prevention

* Mutual Exclusion

  * 공유해서는 안 되는 자원의 경우 반드시 성립해야 함

* Hold and Wait

  * 프로세스가 자원을 요청할 때 다른 어떤 자원도 가지고 있지 않아야 한다
  * 방법 1. 프로세스 시작 시 모든 필요한 자원을 할당받게 하는 방법
  * 방법 2. 자원이 필요할 경우 보유 자원을 모두 놓고 다시 요청

* No Preemption

  * process가 어떤 자원을 기다려야 하는 경우 이미 보유한 자원이 선점됨
  * 모든 필요한 자원을 얻을 수 있을 때 그 프로세스는 다시 시작된다
  * State를 쉽게 save하고 restore할 수 있는 자원에서 주로 사용(CPU, memory)

* Circular Wait

  * 모든 자원 유형에 할당 순서를 정하여 정해진 순서대로만 자원 할당

  * 예를 들어 순서가 3인 자원 Ri를 보유 중인 프로세스가 순서가 1인 자원 Rj을 할당받기 위해서는

    우선 Ri를 release해야 한다.

　

### Deadlock Avoidance

* 자원 요청에 대한 부가정보를 이용해서 자원 할당이 deadlock으로부터 안전한지를 동적으로 조사해서

  안전한 경우에만 할당

* 가장 단순하고 일반적인 모델은 프로세스들이 필요로 하는 각 자원별 최대 사용량을 미리

  선언하도록 하는 방법임

* safe state

  * 시스템 내의 프로세스들에 대한 safe sequence가 존재하는 상태

* safe sequence

  * 프로세스의 sequence가 safe하려면 자원요청이 가용자원 + 모든 보유 자원에 의해 충족

