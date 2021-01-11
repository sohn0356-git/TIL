import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr")
table = cursor.fetchall()
for record in table:
    print("이름 : %s, 전화 : %s, 주소 : %s" %record)
print(type(table))
cursor.close()
con.close()