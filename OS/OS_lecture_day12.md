# 운영체제 12일차

　

## Process Synchronization(6-2~6-2)

　

### Monitor

* Semaphore의 문제점

  * 코딩하기 힘들다
  * 정확성의 입증이 어렵다
  * 자발적 협력이 필요하다
  * 한번의 실수가 모든 시스템에 치명적 영향

* 동시 수행중인 프로세스 사이에서 abstract data type의 안전한 공유를

  보장하기 위한 high-level synchronization construct

*  모니터 내에서는 한 번에 하나의 프로세스만이 활동 가능

* 프로그래머가 동기화 제약 조건을 명시적으로 코딩할 필요 없음

* 프로세스가 모니터 안에서 기다릴 수 있도록 하기 위해

  _condition variable_ 사용

　

### Bounded-Buffer Problem

```cpp
monitor bounded_buffer
{
    int buffer[N];
    condition full, empty;
    
    /* condition var은 값을 가지지 않고 자신의 큐에 프로세스를
    매달아서 sleep 시키거나 큐에서 프로세스를 깨우는 역할만 함*/
    
    void produce(int x)
    {
        if there is no empty buffer{
            empty.wait();
        }
        add x to an empty buffer
        full.signal();
	}
    
    void consume(int *x)
    {
        if there is no full buffer{
            full.wait();
        }
        remove an item from buffer and store it to *x
        empty.signal();
    }
}
```

　

### Dining Philosophers Example

```cpp
monitor dining_philosopher
{
    enum { thinking, hungry, eating} state[5];
    condition self[5];
    
    void pickup(int i){
        state[i] = hungry;
        test(i);
        if(state[i] != eating)
        {
            self[i].wait();
        }
    }
    
    void putdown(int i){
        state[i] = thinking;
        test((i+4)%5);
        test((i+1)%5);
    }
    
    void test(int i){
        if((state[(i+4)%5] != eating) && state[i] == hungry && state[(i+1)%5] != eating){
            state[i] = eating;
            self[i].signal();
        }
    }
    
    void init(){
        for(int i=0;i<5;i++)
        {
            state[i] = thinking;
		}
	}
    
    Each Philosopher:
    {
        pickup(i);
        eat();
        putdown(i);
        think();
    } while(1)
    
}
```

