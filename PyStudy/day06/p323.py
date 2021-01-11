import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT addr FROM tblAddr WHERE name = '김상형'")
record = cursor.fetchone()
print("김상형은 %s에 살고 있습니다" % record)

cursor.close()
con.close()