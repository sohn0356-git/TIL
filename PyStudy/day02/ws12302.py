#1. 각 학생의 합과 평균을 출력
#2. 전체 학생의 합과 평균을 출력

data = [
    [100,90,98,88],
    [100,90,98,87],
    [100,90,98,86],
    [100,90,98,85]
]

sum_list = []
cnt = 0

for scores in data:
    score = 0
    for s in scores:
        score += s
        cnt += 1
    sum_list.append(score)

for i in range(len(sum_list)):
    print("개인 성적의 합 : ",sum_list[i],"개인 성적의 평균",sum_list[i]/len(data[0]))

print("전체 학생의 성적의 합 : ", sum(sum_list))
print("전체 학생의 성적의 평균 : ", sum(sum_list)/cnt)
