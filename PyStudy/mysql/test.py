import pymysql

config = {
'user':'CEO',
'password':'111111',
'host':'127.0.0.1',
'database':'shop1',
'port':3306
}

conn = pymysql.connect(**config)
cursor = conn.cursor()
cursor.execute("""SELECT * FROM users""")
table = cursor.fetchall()

print(table)

cursor.close()
conn.close()