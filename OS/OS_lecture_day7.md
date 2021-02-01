# 운영체제 7일차

　

## 스케줄링

　

### CPU-burst Time의 분포

* 여러 종류의 job이 섞여 있기 때문에 CPU 스케줄링이 필요하다
* Interactive job에게 적절한 response 제공 요망
* CPU와 I/O 장치 등 시스템 자원을 골고루 효율적으로 사용

　

### CPU Scheduler & Dispathcer

* CPU Scheduler : ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다.
* Dispathcer : CPU의 제어권을 CPU Scheduler에 의해 선택된 프로세스에게 넘긴다.(Context Switch)
* 상태변화
  	1. Running -> Blocked(ex : I/O 요청하는 시스템 콜)
   	2. Running -> Ready(ex : 할당시간 만료로 timer interrupt)
   	3. Blocked -> Ready(ex : I/O 완료후 인터럽트)
   	4. Terminate
 * 1, 4에서의 스케줄링은 nonpreemiptive(=강제로 빼앗지 않고 자진 반납)
 * All other scheduling is preemiptive(=강제로 빼앗음)

　

### Scheduling Criteria

* CPU utilization(이용률)
* Throughput(처리량)
* Turnaround time(소요시간, 반환시간)
* Waiting time(대기 시간)
* Response time(응답 시간)

　

