data = [1,2,3,4,5] # List
print(data)
sum=0
for d in data:
    sum+= d
    print(d, end = ' ')
print()
print(sum)

datas = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

sum = 0

for dr in datas:
    for dc in dr:
        sum+=dc

print(sum)