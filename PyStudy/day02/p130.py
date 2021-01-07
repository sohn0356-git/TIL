for i in range(2,10,2):
    print(i,"단--------")
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
        if i==6 and j==5:
            break
    if i>=6:
        break