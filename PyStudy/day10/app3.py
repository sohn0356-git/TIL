str = '3+4+5'
strList = '[1,2,3,4,5]'

users = """[
    { 'id' : 'id01', 'name' : 'james'},
    { 'id' : 'id01', 'name' : 'james'},
    { 'id' : 'id01', 'name' : 'james'}
    ] """

for u in eval(users):
    print(u['id'] + " " + u['name'])

us = users
usstr = repr(us)
print(usstr)