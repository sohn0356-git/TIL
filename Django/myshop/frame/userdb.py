import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
cur = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

import frame.db as d 
import frame.sql as s
import frame.value as v

# from frame.db import Db
# from frame.sql import Sql
# from frame.value import User

class UserDb(d.Db):
    def selectone(self, id):
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = s.Sql.userlistone%(id)
        cursor.execute(sql)
        u = cursor.fetchone()
        user = v.User(u[0],u[1],u[2])
        self.close(conn,cursor)
        return user

    def select(self):
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = s.Sql.userlist
        cursor.execute(sql)
        result = cursor.fetchall()
        all = []
        for u in result:
            user = v.User(u[0],u[1],u[2])
            all.append(user)
        self.close(conn,cursor)
        return all
    
    def insert(self, id,pwd,name):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            sql = s.Sql.userinsert % (id, pwd, name)
            cursor.execute(sql)
            cursor.commit()
        except:
            conn.rollback()
            raise Exception
        finally:
            self.close(conn,cursor)

# userlist test function ...........
def userlist_test():
    users = UserDb().select()
    for u in users:
        print(u)

def userlistone_test():
    user = UserDb().selectone('id01')
    print(user)

def userinsert_test():
    UserDb().insert('id00','pwd00','name00')
    userlist_test()

if __name__ == '__main__':
    userlist_test()