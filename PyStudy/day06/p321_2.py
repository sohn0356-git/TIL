import dbutil

# try:
# 1. SQLite에 접속한다.
dbutil.connectDB('addr.db')

# 2. Table을 만든다
dbutil.makeTable('users')

# 3. 사용자 정보를 입력한다
# dbutil.insertUser(tableName = 'users',id = 'id01', pwd = 'pwd07',이름='김말숙',번호='01012340987',주소='경기',나이=22)

# 3-1. 사용자 정보를 수정한다
dbutil.updateUser(tableName = 'users',id = 'id07', pwd = 'pwd077',이름='장말숙',번호='01077720887',주소='제주도',나이=22)

# 3-2. 사용자 정보를 삭제한다.
dbutil.deleteUser(tableName='users',userid='id01')

# 4. 사용자 정보를 조회한다
dbutil.selectUser(tableName='users')

# except:
#     print("Error")
# finally:
# 5. SQLite를 Close한다.
dbutil.closeDB()