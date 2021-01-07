score = []
score1 = [10,20,30,40,50,60,70,80]
score2 = [score1,[10,20,30,40]]

print(score1[1:2])

# sum = 0
# score1[0] = 0
# for s in score2:
#     for i in s:
#         sum += i
#
# print(sum)


score3 = [[1,2,3,4],[5,6,7,8],[9,10]]
print(score3)

for s in score3:
    for i in range(len(s)):
        print(s[i], end='')
        if i<len(s)-1:
            print(',', end= '')
    print('')

sum_list = []
cnt = 0
for s in score3:
    sum_score = 0
    for i in s:
        sum_score += i
        cnt += 1
    sum_list.append(sum_score)
for i in range(len(sum_list)):
    print("sum : ",sum_list[i] ," avg : ", sum_list[i]/len(score3[i]))

print("sum_all : ",sum(sum_list)," avg_all : ",sum(sum_list)/cnt)