import sqlite3

con = None
cursor = None

#1. SQLite에 접속한다
con = sqlite3.connect('addr.db')
cursor = con.cursor()
print("SQLite Connected ...")

#2. Table을 만든다
# cursor.execute("""DROP TABLE IF EXISTS users""")
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id CHAR(16) PRIMARY KEY,
    pwd CHAR(16),
    name CHAR(10),
    phone CHAR(15),
    addr CHAR(20),
    age NUMBER(3))""")
print("Table Created ...")

#3. 사용자 정보를 입력한다.
# cursor.execute("""INSERT INTO users VALUES
# ('id02','pwd02','김말숙','01012345679','부산',25)
# """)
# con.commit()

#4. 사용자 정보를 조회한다.
cursor.execute("""SELECT * FROM users""")
table = cursor.fetchall()
for record in table:
    print("%s %s %s %s %s %d"%(record))

#5. SQLite를 Close한다.


