from sqlitedb import *

class ItemDB(SqliteDB):
    def __init__(self, dbName):
        super().__init__(dbName)

    def insert(self, item):
        """Insert itemtb Table"""
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlInsertItem % item.sqlmap() )
        cc['con'].commit()
        self.close(cc)

    def update(self, item):
        """Update itemtb Table"""
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlUpdateItem % (item.name, item.price, item.id))
        cc['con'].commit()
        self.close(cc)

    def select(self):
        """Select itemtb Table"""
        cc = self.getConnect()
        table = cc['cursor'].execute(Sql.sqlSelectItemAll).fetchall()
        ret = []
        for record in table:
            ret.append(Item(id=record[0], name=record[1], price=record[2]))
            print(record)
        self.close(cc)
        return ret

    def selectOne(self, id):
        cc = self.getConnect()
        record = cc['cursor'].execute(Sql.sqlSelect % id).fetchone()
        self.close(cc)
        return Item(record[0],record[1],record[2],record[3])

    def delete(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlDeleteItem % id)
        cc['con'].commit()
        self.close(cc)
