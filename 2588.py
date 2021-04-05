a = int(input())
b = int(input())

res = a*b

while b>0:
    print(a*(b%10))
    b = b // 10
print(res)