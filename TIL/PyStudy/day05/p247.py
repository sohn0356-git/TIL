def my_filter(n):
    return n>=90


yoil = ["월",'화','수','목','금','토','일']
food = ['갈비탕','순대국','칼국수','삼겹살']
menu = zip(yoil,food)

for y, f in menu:
    print("%s요일 메뉴 : %s"%(y,f))

score = [90,80,60,100]
score2 = filter(lambda x:x>=90,score)
score3 = filter(my_filter,score)
for i in score:
    if i >= 90:
        print(i)

print('---------------------')

for i in score2:
    print(i)

print('---------------------')

for i in score3:
    print(i)
