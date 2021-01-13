import sqlite3


# fruit
#id name qt price grade origin




class FruitDB:

    con = None
    cursor = None
    tableName = 'fruits'
    dbList = ['id','name','grade','price','qt','origin']
    dbListInt = ['price', 'qt']

    # def __init__(self, infos):
    #     self.__id = infos[0]
    #     self.__name = infos[1]
    #     self.__qt = int(infos[2])
    #     self.__price = int(infos[3])
    #     self.__grade = infos[4]
    #     self.__origin = infos[5]

    def __init__(self):
        self.__data = {}
        while True:
            for d in FruitDB.dbList:
                item = input('%s[입력을 원하지 않을 경우 Enter 혹은 Space bar를 눌러주세요] : '%d)
                self.__data[d] = item.strip()
            print()
            for k, v in self.__data.items():
                if v:
                    print('%s : %s' % (k,v), end= ' ')
                else:
                    print('%s : %s' % (k, "X"), end=' ')
            print()
            isOk = input("입력하신 데이터가 맞습니까?[Y/N] : ")
            if isOk == 'Y' or isOk == 'y':
                break

    def query(self):
        FruitDB.select(self.__data)


    def insert(self):
        """Insert User Data"""
        for d in self.__data.values():
            if not d:
                print("입력되지 않은 정보가 있습니다.")
                return

        table = FruitDB.select({'id' : self.__data['id']})
        if table:
            print("중복되는 data가 존재합니다.\n")
            return

        insertSQL = """INSERT INTO %s VALUES ('%s', '%s', %d, %d, '%s', '%s')""" % (
        FruitDB.tableName, self.__data['id'], self.__data['name'], int(self.__data['qt']), int(self.__data['price']), self.__data['grade'], self.__data['origin'])
        FruitDB.cursor.execute(insertSQL)
        FruitDB.con.commit()
        print("데이터가 성공적으로 입력되었습니다!\n")


    def update(self):
        if self.__data.get('id'):
            tableCheck = FruitDB.select({'id': self.__data.get('id')})
            if tableCheck:
                table = FruitDB.select({"id" : self.__data['id']})
                for k, v in self.__data.items():
                    if not v:
                        self.__data[k] = table[k]

                updateSQL = """UPDATE %s
                                SET name = '%s',
                                qt = %d,
                                price = %d,
                                grade = '%s',
                                origin = '%s'
                                WHERE id = '%s'
                                """ % (FruitDB.tableName, self.__data['name'], int(self.__data['qt']), int(self.__data['price']), self.__data['grade'], self.__data['origin'], self.__data['id'])
                FruitDB.cursor.execute(updateSQL)
                print("데이터가 성공적으로 입력되었습니다!\n")
                FruitDB.con.commit()
            else:
                print("해당하는 데이터가 존재하지 않습니다.\n")
        else:
            print('id가 입력되지 않았습니다!\n')



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
    def select(cls, dict={}):
        """Select User Data"""
        selectSQL = ""
        sqlTuple = ()
        for k in FruitDB.dbList:
            v = dict.get(k)
            if v:
                sqlTuple = sqlTuple + (k, ) + (v, )
        if len(sqlTuple)==0:
            selectSQL = """SELECT id, name, grade, price, qt, origin  FROM %s ORDER BY grade,price """ % FruitDB.tableName
        else :
            selectSQL = """SELECT id, name, grade, price, qt, origin FROM %s WHERE """ % FruitDB.tableName
            for i in range(0,len(sqlTuple),2):
                if sqlTuple[i] in FruitDB.dbListInt:
                    selectSQL += "%s = %d" % (sqlTuple[i], int(sqlTuple[i + 1]))
                else:
                    selectSQL += "%s = '%s'" % (sqlTuple[i], sqlTuple[i + 1])
                if i+2 < len(sqlTuple):
                    selectSQL += ' and '
                else:
                    selectSQL += " ORDER BY grade,price"

        table = FruitDB.cursor.execute(selectSQL).fetchall()
        ret = {}
        if len(table) == 0:
            print("해당하는 데이터가 없습니다!\n")
        else:
            if not dict.get('id'):

                    print(tuple(FruitDB.dbList))
                    for record in table:
                        print(record)
                    print()
            for i, t in enumerate(table[0]):
                ret[FruitDB.dbList[i]]=t
        return ret

    @classmethod
    def delete(cls, id):
        """Delete User Data"""
        table = FruitDB.select({'id' : id})
        if table:
            deleteSQL = """DELETE FROM %s WHERE id = '%s'""" % (FruitDB.tableName, id)

            FruitDB.cursor.execute(deleteSQL)
            FruitDB.con.commit()
            print("데이터가 성공적으로 삭제되었습니다!\n")

        else :
            print("해당하는 데이터가 존재하지 않습니다.\n")


    @classmethod
    def closeDB(cls):
        """Close SQLite"""
        FruitDB.cursor.close()
        FruitDB.con.close()