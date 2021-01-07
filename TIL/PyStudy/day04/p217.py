import random
score = (10,20,30,40)

t = []
for i in range(6):
    t.append(random.randint(1,45))

tp = tuple(t)
print(tp)