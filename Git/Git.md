# Git

> DVCS, 분산버전관리시스템



## 로컬 저장소 설정

```bash
$ git init
Initialized empty Git repository in C:/Users/sohn0/Desktop/blog/git특강/md/.git/
(master) $
```

* `.git` 숨김 폴더가 생성
* `(master)` 브랜치 표기



## 기본 흐름

* 어떠한 작업 => `$ touch 파일명`

```bash
$ git status
On branch master

No commits yet
# 트래킹이 없었던 파일들
# 버전에 기록된 적 없는 파일들
# => 파일 생성 등

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        1.txt

# 커밋을 할 파일이 없다.
# but, untracted files은 있다.
nothing added to commit but untracked files present (use "git add" to track)
```



### add

```bash
$ git add . # 현재 디렉토리(하위까지)
$ git add a.txt # 특정 파일만
$ git add test/ # 특정 폴더
```



```bash
$ git add .
$ git status
On branch master

No commits yet
# 커밋이 될 변경사항들 (Staging area)
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   1.txt

```



### commit

* 스냅샷, 버전을 새롭게 만듦

```bash
$ git commit -m '커밋메시지'
[master (root-commit) 8ff391b] Add 1.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 1.txt

```

* 해싯값이 고유한 커밋을 의미

  ex) `8ff391ba57be64d8b1f71575c147e6c559bcbe85`

* 커밋메시지는 반드시 현재 작업 내용을 나타낼 수 있도록 잘 작성하는 것이 중요하다!



## 기타 상태 명령어

### status

```bash
$ git status
```



### 커밋 히스토리(log)

```bash
$ git log
$ git log --oneline    # 한 줄로 간략히
8ff391b (HEAD -> master) Add 1.txt
$ git log -2		   #최근 2개의 커밋
$ git log -1 --oneline #최근 2개의 커밋을 한 줄로
```



