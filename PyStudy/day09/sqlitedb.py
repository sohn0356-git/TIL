import sqlite3
from value import *

class Sql:
    sqlCreate = ["""CREATE TABLE IF NOT EXISTS usertb(
                       id CHAR(10) PRIMARY KEY,
                       pwd CHAR(10),
                       name CHAR(10),
                       age NUMBER(3)
                   )"""
                   ,
                   """CREATE TABLE IF NOT EXISTS itemtb(
                        id CHAR(10) PRIMARY KEY,
                        name CHAR(10),
                        price NUMBER(10)
                    )"""]
    sqlInsertUser = """INSERT INTO usertb VALUES ('%s', '%s', '%s', %d)"""
    sqlSelectUserAll = """SELECT * FROM usertb ORDER BY id"""
    sqlSelectUser = """SELECT * FROM usertb WHERE id = '%s'"""
    sqlUpdateUser = """UPDATE usertb SET pwd = '%s', name = '%s', age = %d WHERE id = '%s'"""
    sqlDeleteUser = """DELETE FROM usertb WHERE id = '%s'"""

    sqlInsertItem = """INSERT INTO itemtb VALUES ('%s', '%s', %d)"""
    sqlSelectItemAll = """SELECT * FROM itemtb ORDER BY id"""
    sqlSelectItem = """SELECT * FROM itemtb WHERE id = '%s'"""
    sqlUpdateItem = """UPDATE itemtb SET pwd = '%s', name = '%s', price = %d WHERE id = '%s'"""
    sqlDeleteItem = """DELETE FROM itemtb WHERE id = '%s'"""

class SqliteDB:

    def __init__(self, dbName):
        SqliteDB.__dbName = dbName

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
        for sql in Sql.sqlCreate:
            cc['cursor'].execute(sql)
        cc['con'].commit()
        self.close(cc)



