d =[1,2,3]

def f1(d):
    d[0] = 100
    return d

c = f1(d)
print(d)
print(c)