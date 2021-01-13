from sqlitedb import *
from value import *

print('start ...')
sqldb = SqliteDB('udb.db')
sqldb.makeTable()
user = User('id02','pwd02','james',28)
# sqldb.insert(user)
# t = sqldb.selectOne('id01')
t = sqldb.select()
# sqldb.delete('id01')
print('end ...')

