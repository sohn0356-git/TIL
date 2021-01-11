import sqlite3

db = ""
con = None
cursor = None

def connectDB(dbName):
    """Connect SQLite... """
    global db, con, cursor
    db = dbName
    con = sqlite3.connect(dbName)
    cursor = con.cursor()

def makeTable(tableName):
    """Make users Table"""
    global cursor
    cursor.execute("""CREATE TABLE IF NOT EXISTS %s
     (id CHAR(16) PRIMARY KEY,
    pwd CHAR(16),
    name CHAR(10),
    phone CHAR(15),
    addr CHAR(20),
    age NUMBER(3))
     """ % tableName)

def insertUser(**user):
    """Insert User Data"""
    global con, cursor
    tableName = user['tableName']
    insertSQL = """INSERT INTO %s VALUES ('%s','%s','%s','%s','%s',%d)"""%(tableName,user['id'],user['pwd'],user['이름'],user['번호'],user['주소'],user['나이'])
    cursor.execute(insertSQL)
    con.commit()

def updateUser(**user):
    """Update User Data"""
    global con, cursor
    tableName = user['tableName']
    updateSQL = """UPDATE %s
                 SET pwd = '%s',
                 name = '%s',
                 phone = '%s',
                 addr = '%s',
                 age = %d
                 WHERE id = '%s'
                 """ % (tableName, user['pwd'], user['이름'],user['번호'],user['주소'],user['나이'],user['id'])
    cursor.execute(updateSQL)

    con.commit()

def deleteUser(tableName, userid):
    """Delete User Data"""
    global con, cursor
    insertSQL = """DELETE FROM %s WHERE id = '%s'""" % (tableName, userid)
    cursor.execute(insertSQL)
    con.commit()


def selectUser(tableName, userid=""):
    """Select User Data"""
    global cursor
    selectSQL = """SELECT * FROM %s WHERE id = '%s' ORDER BY id ASC""" % (tableName, userid)
    if not userid:
        selectSQL = """SELECT * FROM %s ORDER BY id ASC""" % tableName

    table =  cursor.execute(selectSQL).fetchall()

    for record in table:
        print(record)

def closeDB():
    """Close SQLite"""
    global con, cursor
    cursor.close()
    con.close()