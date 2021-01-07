#1. 데이터의 합과 평균을 구하시오
#2. A~F학점을 출력하시오

data = [98,87,90,34,56,43]
sum = 0
for d in data:
    sum+=d

avg = sum/len(data)
if avg>=90:
    print("A")
elif avg>=80:
    print("B")
elif avg>=70:
    print("C")
elif avg>=60:
    print("D")
else:
    print("F")

