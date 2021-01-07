

def myfilter(n):
    return n/2

score = [90,80,60,100]

for i in map(myfilter,score):
    print(i)