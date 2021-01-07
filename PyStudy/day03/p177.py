import re
s = 'python programming'
print(type(s))
print(type(s[0]))

print(type(s.find('o')))
print(s.find('o'))

for i in re.finditer('o',s):
    print(i.start())

if s.startswith('python'):
    print("True")