# 운영체제 10일차

　

## Process Synchronization

　

### Race condition

* kernel 수행 중 인터럽트 발생 시

* Process가 system call을 하여 kernel mode로 수행 중인데

  context switch가 일어나는 경우

  * 해결책 : 커널모드에서 수행 중일 때는 CPU를 preempt하지 않음

* Multiprocessor에서 shared memory 내의 kernel data

　

### Process Synchronization

* 공유 데이터(shared data)의 동시 접근은 데이터의 불일치 문제를 발생시킬 수 있다
* 일관성 유지를 위해서는 협력 프로세스 간의 실행 순서를 정해주는 메커니즘 필요
* Race condition
  * 여러 프로세스들이 동시에 공유 데이터를 접근하는 상황
  * 데이터의 최종 연산 결과는 마지막에 그 데이터를 다룬 프로세스에 따라 달라짐
* race condition을 막기 위해서는 concurrent process는 동기화되어야 한다.

　

### Critical-Section Problem

* n개의 프로세스가 공유 데이터를 동시에 사용하기를 원하는 경우

* 각 프로세스의 code segment에는 공유 데이터를 접근하는 코드인 Critical Section이 존재

* 하나의 프로세스가 critical section에 있을 때 다른 모든 프로세스는 critial section에

  들어갈 수 없어야 한다.

　

### Initial Attepmts to Solve Problem

```cpp
do{
    entry section
    critical section
    exit section
    remainder section
} while(1);
```

　

#### Algorithm 1

```c++
do{
    while(turn!=0);
    critical section
    turn = 1;
    remainter section
} while(1);
```

* 과잉양보 : 반드시 한번씩 교대로 들어가야만 함 (swap-turn)

  상대방이 turn을 내 값으로 바꿔줘야만 내가 들어갈 수 있음

  특정 프로세스가 더 빈번히 crtical section을 들어가야 한다면?

　

### 프로그램적 해결법의 충족 조건

* Mutual Exclusion(상호 배제)

  * 프로세스 Pi가 critical section 부분을 수행중이면 다른 모든 프로세스들은 그들의 critical section에 들어가면 안 된다.

* Progress

  * 아무도 critical section에 있지 않은 상태에서 critical secition에 들어가고자 하는 프로세스가 있으면

    critical section에 들어가게 해 주어야 한다.

* Bounded Waiting

  * 프로세스가 critical section에 들어가려고 요청한 후부터 그 요청이 허용될 때까지 다른 프로세스들이 critical section에

    들어가는 횟수에 한계가 있어야 한다.

　

#### Algorithm2

```c++
do{
    flag[i] = true;
    while(flag[j]);
    critical section
    flag[i] = false;
    remainder section
} while(1);
```

* Synchronization variables
* 둘 다 2행까지 수행후 끊임 없이 양보하는 상황 발생 가능

　

#### Algorithm3

```c++
do{
    flag[i] = true;
    turn = j;
    while(flag[j] && turn == j);
    critical section
    flag[i] = false;
    remainder section
} while(1);
```

* Combined synchronization variables of algorithms 1 and 2
* Meets all three requirements;
* *Busy Waiting!*

　

### Synchronization Hardware

```c++
do{
    while(Test_and_Set(lock));
    critical section
    lock = false;
    remainder section
} while(1);
```

* 하드웨어적으로 Test & modify를 atomic하게 수행할 수 있도록 지원하는 경우 앞의 문제는 간단히 해결

　

### Semaphores

* 앞의 방식들을 추상화시킴

* Semaphore S

  * integer variable

  * 아래의 두 가지 atomic 연산에 의해서만 접근 가능

    ```c++
    P(S): while(S<=0) do no-op;	//자원을 획득하는 과정
    	  S--;
    ```

    * If positive, decrement-&-enter
    * Otherwise, wait until positive(busy-wait)

    ```c++
    V(S): S++;	//자원을 반납하는 과정
    ```

　

### Critical Section of n Processes

```C++
semaphore mutex;

do{
    P(mutex);
    critical section
    V(mutex);
    remainder section
} while(1);
```

　

### Block/Wakeup Implementation

* Semaphore를 다음과 같이 정의

```c++
typedef struct{
  int value;
    struct process *L;
}semaphore;
```

　

* block과 wakeup을 다음과 같이 가정

  * block : 커널은 block을 호출한 프로세스를 suspend시킴

    이 프로세스의 PCB를 semaphore에 대한 wait queue에 넣음

  * wakeup(P) : block된 프로세스 P를 wakeup시킴

    이 프로세스의 PCB를 ready queue에 넣음

　

### Implementation

```c++
P(S):    S.value--;
		 if(S.value<0)
         {
             add this process to S.L;
             block();
         }
```

　

```c++
V(S):    S.value++;
		 if(S.value <= 0)
         {
             remove a proces P from S.L;
             wakeup(P);
         }
```

　

### Two Types of Semaphores

* Counting semaphore
* Binary semaphore