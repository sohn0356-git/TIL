DATA = 100

def calcsum(datas):
    sum = 0
    for d in datas:
        sum += d
    return sum
def printD():
    print(DATA)
def f2(d=[1],s=0,e=0):
    """

    :param d: List
    :param s: start idx
    :param e: end idx
    :return: sum of start~end
    """
    avg = 0
    for i in range(s,e+1):
        avg+=d[i]
    avg/=(e-s+1)
    return avg;

def f4(*argv):
    print(type(argv))
    for i in argv[0]:
        print(type(i),sep=' ')
        print(i)
def f5(begin=1, end=1, step=1):
    sum = 0
    for i in range(begin,end+1,step):
        sum+=i
    return sum

def f6(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']
    return f5(begin,end,step)

def f8(n, *m, **a):
    print(n)
    print(m)
    print(a)

    print(type(n))
    print(type(m))
    print(type(a))



datas = [1,2,3,4,5]
print(calcsum(datas))
print(sum(datas))

def f1(n):
    sum = 0
    for i in range(n):
        sum+=i
    return sum