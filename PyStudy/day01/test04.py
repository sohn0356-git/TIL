a = input()
sum = 0
if(a.isdigit()):
    for i in range(1,1+int(a)):
        c = input()
        if (c.isdigit()):
            sum +=int(c)
        else:
            a = '0'
            break
    if a!='0':
        print("sum : ",sum," avg : ",sum/int(a))