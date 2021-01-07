score = [90,80,60,100]
score2 = sorted(score,reverse=True)
for i, s in enumerate(score2,1):
    print("%d등 : %d점"%(i,s))