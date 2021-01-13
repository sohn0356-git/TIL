import sqlite3
from value import User

class Sql:
    sqlCreate = """CREATE TABLE IF NOT EXISTS usertb(
               id CHAR(10) PRIMARY KEY,
               pwd CHAR(10),
               name CHAR(10),
               age NUMBER(3)
           )"""
    sqlInsert = """INSERT INTO usertb VALUES ('%s', '%s', '%s', %d)"""
    sqlSelectAll = """SELECT * FROM usertb"""
    sqlSelect = """SELECT * FROM usertb WHERE id = '%s'"""
    sqlUpdate = """UPDATE usertb SET pwd = '%s', name = '%s', age = %d WHERE id = '%s'"""
    sqlDelete = """DELETE FROM usertb WHERE id = '%s'"""

class SqliteDB:
    def __init__(self, dbName):
        self.__dbName = dbName

    def getConnect(self):
        con = sqlite3.connect(self.__dbName)
        cursor = con.cursor()
        # print(self.__dbName + 'Connected ...')
        return {'con':con, 'cursor' : cursor}

    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close()
        if cc['con'] != None:
            cc['con'].close()

    def makeTable(self):
        """Make usertb Table"""
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlCreate)
        cc['con'].commit()
        self.close(cc)

    def insert(self, u):
        """Insert usertb Table"""
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlInsert % u.sqlmap() )
        cc['con'].commit()
        self.close(cc)

    def update(self, u):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlUpdate % (u.pwd, u.name, u.age, u.id))
        cc['con'].commit()
        self.close(cc)

    def select(self):
        cc = self.getConnect()
        table = cc['cursor'].execute(Sql.sqlSelectAll).fetchall()
        user = []
        for record in table:
            user.append(User(id=record[0], pwd=record[1], name=record[2], age=record[3]))
            print(record)
        self.close(cc)
        return user

    def selectOne(self, id):
        cc = self.getConnect()
        record = cc['cursor'].execute(Sql.sqlSelect % id).fetchone()
        self.close(cc)
        return User(record[0],record[1],record[2],record[3])

    def delete(self, id):
        cc = self.getConnect()
        record = cc['cursor'].execute(Sql.sqlDelete % id)
        cc['con'].commit()
        self.close(cc)

