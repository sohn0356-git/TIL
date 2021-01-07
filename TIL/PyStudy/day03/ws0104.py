import random
#Number Guess Game

#1. 두 자리의 숫자 2개를 입력 받는다
#2. 두 수 사이의 랜덤한 숫자를 발생시킨다.
#3. 넘버 게임을 시작한다.
#4. 숫자를 입력 받아 2번에서 만들어진 숫자를 기준으로 3가지의 조건을 출력한다.
#   크다, 작다, 맞다
#5. 게임 한 횟수를 화면에 출력한다.(게임 횟수 제한을 둔다. 횟수는 10회)
#6. 10회가 넘으면 FAIL
#7. 숫자가 맞으면 새로운 게임을 다시 만들어 시작 할 수 있다.

while True:
    print("_______________New Game Start________________")
    input_list = input("두 수를 입력하세요 : ")
    if input_list.find(' ')==-1:
        print('두 수를 입력하세요\n\n\n\n\n')
    else:
        input_list = input_list.split(' ')
        if len(input_list)==2:
            i1 = input_list[0]
            i2 = input_list[1]
            if i1.isdecimal() and i2.isdecimal():
                i1 = int(i1)
                i2 = int(i2)
                if i1>i2:
                    i1,i2 = i2,i1
                if i1>9 and i2<100:
                    while True:
                        ans = random.randint(i1,i2)
                        cnt = 10
                        while cnt>0:
                            i = input("Guess : ")
                            if i.isdecimal():
                                i = int(i)
                                if i>ans:
                                    print("크다")
                                elif i<ans:
                                    print("작다")
                                else:
                                    print("정답!!\n\n\n\n\n")
                                    break
                            else:
                                print("숫자만 입력하세요")
                            cnt-=1
                            if cnt==0:
                                print("Fail!!\n\n\n\n\n")
                            else:
                                print("남은 기회 : %5d" % cnt)
                        if cnt>0:
                            break
                        else:
                            print("%3d와 %3d사이에서 숫자를 재생성합니다"%(i1,i2))
                else:
                    print("두 자리 숫자 2개를 입력하세요!\n\n\n\n\n")
            else:
                print("숫자만 입력하세요\n\n\n\n\n")
        else:
            print('두 수를 입력하세요\n\n\n\n\n')
