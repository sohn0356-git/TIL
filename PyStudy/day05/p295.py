import myutil1

d = -5

try:
    s = myutil1.calc(d)
    print(s)
except ZeroDivisionError:
    print('zero division error')
except ValueError:
    print("value error")