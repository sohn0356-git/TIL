import dbutil

print('Start ...')


try:
    dbutil.connectDB('addr.db')
    while True:
        menu = input('Input Menu(c,r,ro,u,d,q) ...')
        menu = menu.lower()
        if menu == 'q':
            dbutil.closeDB()
            print("exit")
            break
        elif menu == 'c':
            infos = input('Input User Data ...').split(' ')
            dbutil.insertUser(tableName = 'users',id = infos[0], pwd = infos[1],이름= infos[2],번호=infos[3],주소=infos[4],나이=int(infos[5]))
        elif menu == 'r':
            dbutil.selectUser(tableName='users')
        elif menu == 'ro':
            id = input('Select Users id ...')
            dbutil.selectUser(tableName='users', userid=id)
        elif menu == 'u':
            infos = input('Input User Data ...').split(' ')
            dbutil.updateUser(tableName = 'users',id = infos[0], pwd = infos[1],이름= infos[2],번호=infos[3],주소=infos[4],나이=int(infos[5]))
        elif menu == 'd':
            print('Select User id')
            dbutil.deleteUser(tableName='users', userid='id01')
except:
    print("error")
finally:
    dbutil.closeDB()


print('End ...')