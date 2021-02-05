# 운영체제 8일차

　

## 스케줄링

　

### FCFS(First-Come First-Served)

* 프로세스의 도착 순서대로 처리하는 방법
* Convoy effect : short process behind long process

　

### SJF(Shortest-Job-First)

* 각 프로세스의 다음번 CPU burst time을 가지고 스케줄링에 활용
* CPU burst time이 가장 짧은 프로세스를 제일 먼저 스케줄
* 주어진 프로세스들에 대해 minimum average waiting time을 보장

　

### SRTF(Shortest-Remaining-Time-First)

* SJF에서 Preemptive하게 스케줄하는 방식을 SRTF라 한다.

　

> 다음 CPU Burst Time의 예측

* 추정(estimate)만이 가능하다
* 과거의 CPU burst time을 이용해서 추정

　

### Priority Scheduling

* A priority number is associated with each process
* highest prioirity를 가진 프로세스에게 CPU 할당
* SJF는 일종의 Priority Scheduling이다
* Problem : Starvation
* Solution : Aging -> as time progresses increase the priority of the process

　

### Round Robin(RR)

* 각 프로세스는 동일한 크기의 할당 시간을 갖는다

* 할당 시간이 지나면 프로세스는 선점(preempted)당하고 ready queue의 제일 뒤에 가서 다시 줄을 선다.

* n개의 프로세스가 ready queue에 있고 할당 시간이 q  time unit인 경우 각 프로세스는 최대 q time unit

  단위로 CPU시간의 1/n을 얻는다.

* 일반적으로 SJF보다 average turnaround time이 길지만 response timedms 더 짧다.

　

