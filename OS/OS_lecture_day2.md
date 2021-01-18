# 운영체제 2일차

　

* CPU 스케줄링
  * FCFS(First-Come-First-Served) => 얼핏 공평해보이지만 비효율적이다!
  * SJF(Shortest-Job-First)) 
    * minimum average waiting time을 보장!
    * Starvation(기아 현상) 발생 가능
  * RR(Round-Robin)
    * 각 프로세스가 동일한 크기의 CPU 할당시간을 가짐
    * 대기시간이 프로세스의 CPU 사용시간에 비례

　

* 메모리 관리

  CPU가 1,1,1,1,2,2,3,3,2,4,5,현재... 요청(Now, disk is full)

  * LRU(가장 오래전에 참조 페이지 삭제)
    * 페이지 1을 삭제
  * LFU(참조횟수가 가장 적은 페이지 삭제)
    * 페이지 4를 삭제

　

* 디스크 접근 시간의 구성
  * 탐색시간
    * 헤드를 해당 트랙(실린더)으로 움직이는데 걸리는 시간
  * 회전지연
    * 헤드가 원하는 섹터에 도달하기까지 걸리는 시간
  * 전송시간
    * 실제 데이터의 전송시간
* 디스크 스케줄링
  * seek time을 최소화하는 것이 목표
  * seek time ~ seek distance
  * SSTF(Shortest Seek Time First)
    * Starvation(기아 현상) 발생 가능
  * SCAN
    * 헤드가 디스크의 한쪽 끝에서 다른쪽 끝으로 이동하며 가는 길목에 있는 모든 요청을 처리
    * ex) 엘리베이터

　

* 저장장치 계층구조와 캐싱
  * Primary : Registers, Cache Memory, Main Memory
  * Secondary : Magentic Disk, Optical Disk, Magnetic Tape



* 운영체제의 종류
  * 서버용, PC용, 스마트디바이스용 운영체제
  * 공개 소프트웨어 (Open Source Software)
    * ex) Linux, Android