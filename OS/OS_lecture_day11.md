# 운영체제 11일차

　

## Process Synchronization(6-1~6-1)

　

### Deadlock and Starvation

* Deadlock : 둘 이상의 프로세스가 서로 상대방에 의해 충족될 수 있는 event를 무한히 기다리는 현상
* Starvation : 프로세스가 suspend된 이유에 해당하는 세마포어 큐에서 빠져나갈 수 없는 현상

　

### Classcial Problems of Synchronization

* Bounded-Buffer Problem(Producer-Consumer Problem)
  * shared data : buffer 자체 및 buffer 조작 변수(empty/full buffer의 시작 위치)
  * Synchronization variables 
    * mutual exclusion
    * resource count

```cpp
//Producer
do{
    produce an item in x
        ...
    P(empty);
    P(mutex);
    	...
    add x to buffer
        ...
    V(mutex);
    V(full);
} while(1);

//Consumer
do{
    P(full);
    P(mutex);
	    ...
	remove an item from buffer to y
        ...
    V(mutex);
    V(full);
    	...
    consume the item in y
} while(1);
```

　

### Readers-Writers Problem

* 한 process가 DB에 write중일 때 다른 process가 접근하면 안됨
* read는 동시에 여럿이 해도 됨
* solution
  * Writer가 DB에 접근 허가를 아직 얻지 못한 상태에서는 모든 대기중인 Reader들이 다 DB에 접근하게 해준다.
  * Writer는 대기 중인 Reader가 하나도 없을 때 DB 접근이 허용된다.
  * 일단 Writer가 DB에 접근 중이면 Reader들은 접근이 금지된다.
  * Writer가 DB에서 빠져나가야만 Reader의 접근이 허용된다.
* Shared data
  * DB 자체
  * readcount;
* Synchronization variables
  * mutex	/* 공유 변수 readcount를 접근하는 코드의 mutual exclusion 보장을 위해 사용 */
  * db           /*  Reader와 writer가 공유 DB 자체를 올바르게 접근하는 역할 */

```cpp
//Writer

P(db);
	...
writing DB is performed
    ...
V(db);

/* Starvation 발생 가능 */

//Reader
P(mutex);
readercount++;
if(readcount==1)
{
    P(db);
}
V(mutex);
	...
reading DB is performed
    ...
P(mutex);
readcount--;
if(readcount==0)
{
    V(db);
}
V(mutex);
```

　

### Dining-Philosophers Problem

```cpp
semaphore chopstick[5];

Philosopher i
do{
    P(chopstick[i]);
    P(chopstick[(i+1)%5]);
    ...
    eat();
    ...
    V(chopstick[i]);
    V(chopstick[(i+1)%5]);
    ...
    think();
    ...
} while(1);
```

* 앞의 solution의 문제점
  * deadlock 가능성이 있다
  * 모든 철학자가 동시에 배가 고파져 왼쪽 젓가락을 집어버린 경우
* 해결방안
  * 4명의 철학자만이 테이블에 동시에 앉을 수 있도록 한다.
  * 젓가락을 두 개 모두 집을 수 있을 때에만 젓가락을 집을 수 있게 한다.
  * 비대칭 : 짝수(홀수) 철학자는 왼쪽(오른쪽) 젓가락 부터 잡게 한다.

```cpp
Philosopher i
do{
    pickup(i);
    eat();
    putdown(i);
    think();
} while(1);

void putdown(int i){
    P(mutex);
    state[i] = thinking;
    test((i+4)%5);
    test((i+1)%5);
    V(mutex);
}

void pickup(int i){
	P(mutex);
    state[i] = hungry;
    test(i);
    V(mutex);
    P(self[i]);
}

void test(int i){
	if(state[(i+4)%5]!=eating && state[i]==hungry && state[(i+1)%5]!=eating)
    {
        state[i] = eating;
        V(self[i]);
	}
}
```

