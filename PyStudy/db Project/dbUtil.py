import sqlite3


# fruit
#id name qt price grade origin

class FruitDB:

    con = None
    cursor = None
    tableName = 'fruits'
    dbList = ['id','name','qt','price','grade','origin']

    def __init__(self, infos):

        # for d in FruitDB.dbList:
        #     item = input('%s : '%d)
        #     self.data[d] = item
        self.__id = infos[0]
        self.__name = infos[1]
        self.__qt = int(infos[2])
        self.__price = int(infos[3])
        self.__grade = infos[4]
        self.__origin = infos[5]

    def insert(self):
        """Insert User Data"""
        insertSQL = """INSERT INTO %s VALUES ('%s', '%s', %d, %d, '%s', '%s')""" % (
        FruitDB.tableName, self.__id, self.__name, self.__qt, self.__price, self.__grade, self.__origin)
        FruitDB.cursor.execute(insertSQL)
        FruitDB.con.commit()

    def update(self):
        updateSQL = """UPDATE %s
                        SET name = '%s'
                        qt = %d,
                        price = %d,
                        grade = '%s',
                        origin = '%s'
                        WHERE id = '%s'
                        """ % (FruitDB.tableName, self.__name, self.__qt, self.__price, self.__grade, self.__origin, self.__id)
        FruitDB.cursor.execute(updateSQL)

    @classmethod
    def connectDB(cls):
        """Connect SQLite... """
        FruitDB.con = sqlite3.connect('order.db')
        FruitDB.cursor = FruitDB.con.cursor()

    @classmethod
    def makeTable(cls):
        """Make users Table"""
        makeSQL = """CREATE TABLE IF NOT EXISTS fruits(
                    id CHAR(16) PRIMARY KEY,
                    name CHAR(16),
                    qt NUMBER(5),
                    price NUMBER(10),
                    grade CHAR(15),
                    origin CHAR(20)) """
        FruitDB.cursor.execute(makeSQL)

    @classmethod
    def select(cls, name=""):
        """Select User Data"""
        selectSQL = """SELECT * FROM %s WHERE name = '%s'""" % (FruitDB.tableName, name)
        if not name:
            selectSQL = """SELECT * FROM %s ORDER BY grade """ % FruitDB.tableName

        table = FruitDB.cursor.execute(selectSQL).fetchall()

        for record in table:
            print(record)

        FruitDB.con.commit()

    @classmethod
    def delete(cls, id):
        """Delete User Data"""
        deleteSQL = """DELETE FROM %s WHERE id = '%s'""" % (FruitDB.tableName, id)
        FruitDB.cursor.execute(deleteSQL)
        FruitDB.con.commit()


    @classmethod
    def closeDB(cls):
        """Close SQLite"""
        FruitDB.cursor.close()
        FruitDB.con.close()