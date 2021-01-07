a = 1
b = a

print(a==b)
print(a is b)

l1 = [1,2,3,4]
l2 = l1
l3 = l1.copy()

print(l1==l2)
print(l1 is l2)

print(l1==l3)
print(l1 is l3)