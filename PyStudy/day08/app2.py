from sqlitedb import *
from value import *

sqldb = SqliteDB('udb.db')

userList = sqldb.select()
for u in userList:
    print(u)

user = User('id02','1111','kim',30)
sqldb.update(user)
print("______________________________")

userList = sqldb.select()
for u in userList:
    print(u)