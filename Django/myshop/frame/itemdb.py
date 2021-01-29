# import frame.db as d 
# import frame.sql as s
# import frame.value as v

from frame.db import *
from frame.sql import Sql
from frame.value import Item

class ItemDb(Db):
    def selectone(self, id):
        id = int(id)
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = Sql.itemlistone%(id)
        cursor.execute(sql)
        i = cursor.fetchone()
        item = Item(i[0],i[1],i[2],i[3],i[4])
        self.close(conn,cursor)
        return item

    def select(self):
        conn = self.getConnection()
        cursor = conn.cursor()
        sql = Sql.itemlist
        cursor.execute(sql)
        result = cursor.fetchall()
        all = []
        for i in result:
            item = Item(i[0],i[1],i[2],i[3],i[4])
            all.append(item)
        self.close(conn,cursor)
        return all
    
    def insert(self, name, price, imgname):
        try:
            price = int(price)
            conn = self.getConnection()
            cursor = conn.cursor()
            sql = Sql.iteminsert % (name, price, imgname)
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            raise Exception
        finally:
            self.close(conn,cursor)

    def delete(self, id):
        try:
            id = int(id)
            conn = self.getConnection()
            cursor = conn.cursor()
            sql = Sql.itemdelete % (id)
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            raise Exception
        finally:
            self.close(conn,cursor)

    def update(self,id, name, price, imgname):
        try:
            id = int(id)
            price = int(price)
            conn = self.getConnection()
            cursor = conn.cursor()
            sql = Sql.itemupdate % (name, price, imgname, id)
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            raise Exception
        finally:
            self.close(conn,cursor)

# itemlist test function ...........
def itemlist_test():
    items = ItemDb().select()
    for u in items:
        print(u)

def itemlistone_test():
    item = ItemDb().selectone('id01')
    print(item)


if __name__ == '__main__':
    itemlist_test()