gender = input("성별을 입력하세요 : ")
height = input("키를 입력하세요 : ")
weight = input("몸무게를 입력하세요 : ")

if height.isnumeric() and weight.isnumeric():
    height = int(height)/100
    weight = int(weight)

    BMI = weight/(height**2)
    if BMI<20:
        print("저체중")
    elif BMI<25:
        print("정상")
    elif BMI<30:
        print("과체중")
    else:
        print("비만")