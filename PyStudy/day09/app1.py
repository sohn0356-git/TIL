from userdb import *
from itemdb import *

# 1. 사용하고자 하는 데이터베이스 이름을 설정
# 2. 테이블을 생성 (단, 존재하지 않을 경우에만)
# 3. 사용자 테이블을 사용하기 위해 userdb 객체를 이용하여 CRUD 진행

def userInsert(user):
    userdb = UserDB('shopdb.db')
    userdb.insert(user)

def init():
    userdb = UserDB('shopdb.db')
    return userdb.select()


if __name__ == "__main__":
    sqlitedb = SqliteDB('shopdb.db')
    userdb = UserDB('shopdb.db')
    itemdb = ItemDB('shopdb.db')
    userdb.makeTable()

    user = User('id04','pwd04','james',25)
    # userdb.insert(user)
    userdb.select()

    print('--------------------------------------')

    item = Item('id01','apple',500)
    # ItemDB.insert(item)
    itemdb.select()

