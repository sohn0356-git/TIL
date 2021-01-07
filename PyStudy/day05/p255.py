a = 10

def f1(a):
    a += 5
    return a

print(a)
b = f1(5)
print(a)
print(b)

if a==b:
    print('ok')
if a is b:
    print('ok')