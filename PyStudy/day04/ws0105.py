import random
#Lotto Game

#1. 시나리오
# 사용자로부터 6가지 숫자를 입력받는다.
# 당첨금 누적시스템
# 3등까지 당첨금 지급
# 단, 1등 상금은 4개 이상 맞춘 사람만 받을 수 있음
# 금액 범위 (100~10,000)
# 본인 포함 100명의 참가자

#2. 전제 조건 :
#  - 당첨금은 랜덤하게 만든다.
#  - 당첨 번호는 랜덤하게 만든다.
#  - 순위에 따라 당첨금을 차등 지급한다.
#  - 게임을 끝내고 다시 시작할 수 있다.



def print_waring():
    """ 조건에 맞지 않는 Input이 들어왔을 경우 """
    print("1~45의 숫자 6개를 중복되지 않게 다시 입력해주세요")

def gen_lotto():
    """ 1~45의 중복되지 않는 6개의 숫자 list를 return """
    visited = [0]*46
    ret = []
    while len(ret)<6:
        next = random.randint(1,45)
        if visited[next]==0:
            visited[next] = 1
            ret.append(next)
    return ret

def get_prize(i, n):
    """
     상금을 주어진 조건에 맞춰서 분배
     1등상의 경우 4개 이상 맞춘 사람만 받을 수 있음
     2등상의 경우 2개 이상 맞춘 사람만 받을 수 있음
    """
    ret = 0
    for idx in range(len(acc_price)):
        if i<4 and idx==0:
            continue
        if i<2 and idx<2:
            continue
        if acc_price[idx]==0:
            continue
        ret = acc_price[idx]
        acc_price[idx] = 0
        break
    return int(ret/n)

#Lotto Game이 진행된 회차
week = 1

# 누적된 상금을 저장하는 List
acc_price = [0] * 3 # 3등까지 당첨금

# User를 포함한 100명의 Lotto번호를 저장하는 List
guest = [[] for i in range(100)]

while True:

    # 금번 발생한 상금을 내림차순으로 저장하는 List
    price = []
    for i in range(3):
        price.append(random.randint(100, 10000))
    price.sort(reverse=True)

    # 상금을 축적
    for i in range(3):
        acc_price[i] += price[i]

    print("\n\n\n1조의 ",week,"번째 Lotto Game을 찾아주셔서 감사합니다. 현재 누적 상금은",sep='')
    print("1등 : %d만원\n2등 : %d만원\n3등 : %d만원입니다\n\n\n"%(acc_price[0],acc_price[1],acc_price[2]))

    # Key : Lotto Game 참여자의 맞춘 번호의 수
    # Value : 참여자의 번호(User의 경우 99번)
    score_board = {6:[],5:[],4:[],3:[],2:[],1:[],0:[]}

    # Lotto 번호를 발생
    lotto = gen_lotto()
    for i in range(99):
        # 참여자의 Lotto번호를 갱신
        guest[i].clear()
        guest[i] = gen_lotto()

    # 사용자의 숫자 입력
    while True:
        user_num = input("중복 안 되는 숫자 입력[6개] : ")
        if user_num.find(' ')==-1:
            print_waring()
        else:
            user_num = user_num.split(' ')
            while user_num.count('')>0:
                user_num.remove('')
            print()
            if len(user_num) != 6:
                print_waring()
                continue
            guest[99].clear()
            for i in range(len(user_num)):
                if user_num[i].isdecimal() and int(user_num[i])>0 and int(user_num[i])<46:
                    guest[99].append(int(user_num[i]))
                else:
                    print_waring()
                    break
            if len(guest[99]) ==6:
                break

    #--------------debug-----------------#
    # for idx, g in enumerate(guest):
    #     print(idx, " : ",g)

    #score_board 갱신
    for idx in range(100):
        cnt = 0
        for n in guest[idx]:
            if n in lotto:
                cnt += 1
        score_board[cnt].append(idx+1)

    #상금 분배
    for i in range(6,0,-1):
        if len(score_board[i]) != 0:
            money = get_prize(i, len(score_board[i]))
            if money==0:
                break
            print("축하드립니다!!!")
            print(score_board[i])
            print("상금 ",money,"만원을 획득하셨습니다!", sep='')

    print("다음 주에 다시 찾아와주세요 >_<")