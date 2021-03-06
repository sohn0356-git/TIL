# import frame.db as d 
# import frame.sql as s
# import frame.value as v

from frame.db import *
from frame.sql import Sql
from frame.value import User

class UserDb(Db):
    def selectone(self, id):
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = Sql.userlistone%(id)
        cursor.execute(sql)
        u = cursor.fetchone()
        user = User(u[0],u[1],u[2])
        self.close(conn,cursor)
        return user

    def select(self):
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = Sql.userlist
        cursor.execute(sql)
        result = cursor.fetchall()
        all = []
        for u in result:
            user = User(u[0],u[1],u[2])
            all.append(user)
        self.close(conn,cursor)
        return all
    
    def insert(self, id,pwd,name):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            sql = Sql.userinsert % (id, pwd, name)
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            raise Exception
        finally:
            self.close(conn,cursor)

    def delete(self, id):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            sql = Sql.userdelete % (id)
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            raise Exception
        finally:
            self.close(conn,cursor)

    def update(self, id,pwd,name):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            sql = Sql.userupdate % (pwd, name, id)
            cursor.execute(sql)
            conn.commit()
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