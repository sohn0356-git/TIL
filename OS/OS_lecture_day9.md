# 운영체제 8일차

　

## 스케줄링

　

### Multilevel Queue

* Ready queue를 여러 개로 분할
  * foreground
  * background
* 각 큐는 독립적인 스케줄링 알고리즘을 가짐
  * foreground - RR
  * background - FCFS
* 큐에 대한 스케줄링이 필요
  * Fixed priority scheduling
  * Time slice

　

### Multilevel Feedback Queue

* 프로세스가 다른 큐로 이동 가능

* 에이징을 이와 같은 방식으로 구현할 수 있다

* Three queues:

  * Q0 - time quantum 8 milliseconds
  * Q1 - time quantum 16 milliseconds
  * Q2 - FCFS

  new job이 queue Q0에 들어감 -> CPU를 잡아서 할당 시간 8 milliseconds동안 수행됨

  -> 다 끝내지 못했으면 queue Q1으로 내려감 -> 16miliseconds동안 수행하고 못 끝내면

  -> queue Q2로 쫓겨남

　

### Multiple-Processor Scheduling

* CPU가 여러 개인 경우 스케줄링은 더욱 복잡해짐
* Homogeneous process
  * Queue에 한 줄로 세워서 각 프로세서가 알아서 꺼내가게 할 수 있다.
  * 반드시 특정 프로세서에서 수행되어야 하는 프로세스가 있는 경우에는 문제가 더 복잡해짐
* Load sharing
  * 일부 프로세서에 job이 몰리지 않도록 부하를 적절히 공유하는 메커니즘 필요
  * 별개의 큐를 두는 방법 vs 공동 큐를 사용하는 방법
* Symmetric Multiprocessing
  * 각 프로세서가 각자 알아서 스케줄링 결정
* Asymmetric multiprocessing
  * 하나의 프로세서가 시스템 데이터의 접근과 공유를 책임지고 나머지 프로세서는 거기에 따름

　

### Real-time Scheduling

* Hard real-time systems
  * Hard real-time task는 정해진 시간 안에 반드시 끝내도록 스케줄링해야 함
* Soft real-time computing
  * Soft real-time task는 일반 프로세스에 비해 높은 priority를 갖도록 해야 함

　

### Thread Scheduling

* Local Scheduling

  * User level thread의 경우 사용자 수준의 thread library에 의해 어떤 thread를 스케줄할지 결정

* Global Scheduling

  * Kernel level thread의 경우 일반 프로세스와 마찬가지로 커널의 단기 스케줄러가 어떤 thread를

    스케줄할지 결정

　

### Algorithm Evaluation

* Queueing models

  * 확률 분포로 주어지는 arrival rate와 service rate등을 통해 각종 preformance index 값을 계산

* Implementation & Measurement

  * 실제 시스템에 알고리즘을 구현하여 실제 작업에 대해서 성능을 측정 & 비교

* Simulation

  * 알고리즘을 모의 프로그램으로 작성 후 trace를 입력으로 하여 결과 비교

  