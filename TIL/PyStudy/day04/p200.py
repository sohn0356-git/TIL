s = [1,2,3,4,5]
print(s[1:3])

print(list(map(lambda x:x*3,s)))

print(s.count(34))

print('ab' in 'abc')

str = ['A','B','C','D','D']

if 'A' in str:
    del str[str.index('A')]
    # str.remove('A')
else:
    str.insert('A')

print(str)