#  파일 입출력 in *Python*

## 파일 쓰기

* open(파일경로, 모드)

  * 모드

  | 모드 |                      설명                      |
  | :--: | :--------------------------------------------: |
  |  r   |  파일을 읽는다. 단, 파일이 없으면 error 발생.  |
  |  w   |    파일에 기록한다. 이미 있을경우 덮어쓴다.    |
  |  a   |           파일에 데이터를 추가한다.            |
  |  x   | 파일에 기록하되 파일이 이미 있으면 error 발생. |

  * 모드 뒤에는 파일의 종류를 지정하는 문자를 쓴다.
    * t : txt 파일
    * b : binary 파일

* write()

```python
f = open("live.txt", "wt", encoding='UTF-8')
f.write("""God will make a way
Where there seems to be no way
He works in ways we cannot see
He will make a way for me
He will be my guide
Hold me closely to his side
With love & strength for each new day
He will make a way
He will make a way
God will make a way
Where there seems to be no way
He works in ways we cannot see
He will make a way for me
He will be my guide
Hold me closely to his side
With love & strength for each new day
He will make a way
He will make a way
By a roadway in the wilderness
He'll lead me
Rivers in the desert
Will I see
Heaven & earth will fade
But his word will still remain
& He will do something new today
God will make a way
Where there seems to be no way
He works in ways we cannot see
He will make a way for me
He will be my guide
Hold me closely to his…
""")
f.close()
```



## 파일 읽기

* 쓰기와 마찬가지로 `open`을 먼저하고 진행한다.
* read()

```python
fr = None
try:
    fr = open("liv.txt","rt", encoding="UTF-8")
    text = fr.read()
    print(text)
except FileNotFoundError:
    print("There isn't file")
finally:
    if fr != None:
        fr.close()
```

> 이 경우 파일의 용량이 크면 메모리를 많이 소모하게 된다.
>
> 다음과 같이 수정해보자

* read(_size)
  * 한 번에 _size만큼의 문자를 읽어온다.

```python
f2 = None
try:
    f2 = open("live.txt","rt")
    while True:
        text = f2.read(10)
        if len(text)==0:
            break
        print(text, end = '')
except FileNotFoundError:
    print("There isn't file")
finally:
    if f2 != None:
        f2.close()
```

* readline()
  * 한 줄씩 읽는 함수로 C++의 getline과 비슷하다.

```python
f = None
try:
    f = open("live.txt","rt")
    text = ""
    line = 1
    while True:
        row = f.readline()
        if not row:
            break
        text += str(line) + " : " + row
        line += 1
    print(text)
except FileNotFoundError:
    print("There isn't file")
finally:
    if f!=None:
	    f.close()
```

* readlines()
  * readline을 파일 전체에 대해 시행한다.

``` python
f = None
try:
    f = open("live.txt","rt")
    rows = f.readlines()
    for row in rows:
        print(row, end = '')
except FileNotFoundError:
    print("There isn't file")
finally:
    if f!=None:
	    f.close()
```

* seek(위치, 기준)
  * 기준이 0이면 처음부터, 2면 끝에서부터, 1이면 현재 위치를 기준으로 한다.

```python
f = None
f = open("live.txt", "rt",encoding="UTF-8")
f.seek(12,0)
text = f.read(10)
print(text)
```

<u>God will mak</u>e a way															=>										e a way


Where there seems to be no way								  	=>										Wh

=> "e a way\nWh"
