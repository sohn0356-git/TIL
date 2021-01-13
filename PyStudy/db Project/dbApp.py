from dbUtil import FruitDB

# DB명 : order.db
# Table명 : fruits

try:
    FruitDB.connectDB()
    if FruitDB.con == None:
        print("Fail")
        exit(1)
    FruitDB.makeTable()
    while True:
        menu = input('Input Menu(c,r,ro,rc,u,d,q) ... ')
        menu = menu.lower()
        if menu == 'q':
            FruitDB.closeDB()
            print("exit")
            break
        elif menu == 'c':
            # infos = input('Input Fruit Data ...').split(' ')
            #name qt price grade origin
            # inputFruit = FruitDB(infos)
            inputFruit = FruitDB()
            inputFruit.insert()
        elif menu == 'r':
            _ = FruitDB.select()
        elif menu == 'ro':
            name = input('Select Fruit name ... ')
            _ = FruitDB.select({'name' : name})
        elif menu == 'rc':
            print("궁금한 사항을 채워넣으세요")
            qry = FruitDB()
            qry.query()
        elif menu == 'u':
            # infos = input('Input Fruit Data ...').split(' ')
            # name qt price grade origin
            # inputFruit = FruitDB(infos)
            inputFruit = FruitDB()
            inputFruit.update()
        elif menu == 'd':
            id = input('Select Fruit id : ')
            FruitDB.delete(id)

except Exception as e:
    print("error ", e)
finally:
    FruitDB.closeDB()
