from sqlitedb import *

class UserDB(SqliteDB):
    def __init__(self, dbName):
        super().__init__(dbName)

    def insert(self, user):
        """Insert usertb Table"""
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlInsertUser % user.sqlmap())
        cc['con'].commit()
        self.close(cc)

    def update(self, user):
        """Update usertb Table"""
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlUpdateUser % (user.pwd, user.name, user.age, user.id))
        cc['con'].commit()
        self.close(cc)

    def select(self):
        """Select usertb Table"""
        cc = self.getConnect()
        table = cc['cursor'].execute(Sql.sqlSelectUserAll).fetchall()
        ret = []
        for record in table:
            ret.append(User(id=record[0], pwd=record[1], name=record[2], age=record[3]))
            print(record)
        self.close(cc)
        return ret

    def selectOne(self, id):
        cc = self.getConnect()
        record = cc['cursor'].execute(Sql.sqlSelectUser % id).fetchone()
        self.close(cc)
        return User(record[0],record[1],record[2],record[3])

    def delete(self, id):
        cc = self.getConnect()
        cc['cursor'].execute(Sql.sqlDeleteUser % id)
        cc['con'].commit()
        self.close(cc)