# 한자리 숫자를 입력 받는다.
# 숫자의 범위는 1~9
# 아니면 프로그램 종료
# 입력 받는 숫자까지의 합과 평균을 구하시오

i = input("한자리 숫자를 입력하세요 : ")
if i.isdigit():
    int_i = int(i)
    if int_i>0 and int_i<10:
        sum = 0
        for n in range(1,int_i+1):
            sum += n
        print("합 : ",sum," 평균 : ",sum/int_i)