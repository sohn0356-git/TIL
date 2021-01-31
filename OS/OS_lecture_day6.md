# 운영체제 6일차

　

## 프로세스

　

### 프로세스 생성

* 부모 프로세스가 자식 프로세스 생성
* 프로세스의 트리(계층 구조)형성
* fork, exec, wait, exit



### 프로세스 종료

* 자식이 할당 자원의 한계치를 넘어섬
* 자식에게 할당된 테스크가 더 이상 필요하지 않음
* 부모가 종료하는 경우



### fork()

```c
int main()
{
    int pid;
    pid = fork();
    if(pid==0)
    {
        printf("\n Hello, I am child!'\n");
        execlp("bin/date", "bin/date",(char *)0);
    }
    else if(pid>0)
    {
        printf("\n Hello, I am parent!'\n");
	}
}
```



### exit()

* 자발적 종료
  * 마지막 statement 수행 후 exit() 시스템 콜을 통해
* 비자발적 종료
  * 부모 프로세스가 자식 프로세스를 강제 종료시킴
  * 키보드 입력으로 kill, break가 들어올 경우
  * 부모 프로세스가 종료되는 경우



### 프로세스 간 협력

* 독립적 프로세스
  * 프로세스는 각자의 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못함
* 협력 프로세스
  * 프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음
* 프로세스 간 협력 메커니즘(IPC : Interprocess communication)
  * 메시지를 전달하는 방법(Message Passing)
  * 주소 공간을 공유하는 방법(Shared Memory)



### Message Passing

* Message system
  * 프로세스 사이에 공유 변수를 일체 사용하지 않고 통신하는 시스템
* Direce Communication
  * 통신하려는 프로세스의 이름을 명시적으로 표시
* Indirect Communication
  * mailbox(또는 port)를 통해 메시지를 간접 전달