from dbUtil import FruitDB

# DB명 : order.db
# Table명 : fruits

# try:
FruitDB.connectDB()
if FruitDB.con == None:
    print("Fail")
    exit(1)
FruitDB.makeTable()
while True:
    menu = input('Input Menu(c,r,ro,u,d,q) ...')
    menu = menu.lower()
    if menu == 'q':
        FruitDB.closeDB()
        print("exit")
        break
    elif menu == 'c':
        infos = input('Input Fruit Data ...').split(' ')
        #name qt price grade origin
        inputFruit = FruitDB(infos)
        inputFruit.insert()
    elif menu == 'r':
        FruitDB.select()
    elif menu == 'ro':
        name = input('Select Fruit name ...')
        FruitDB.select(name)
    elif menu == 'u':
        infos = input('Input Fruit Data ...').split(' ')
        # name qt price grade origin
        inputFruit = FruitDB(infos)
        inputFruit.insert()
    elif menu == 'd':
        id = input('Select Fruit id')
        FruitDB.delete(id)

# except Exception as e:
#     print("error ", e)
# finally:
#     FruitDB.closeDB()
