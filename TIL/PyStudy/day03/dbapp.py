import dbutil

print('start')
while True:
    menu = input('Input menu ... i,s,sa,q ')
    if menu=='q':
        print("exit")
        break
    elif menu=='i':
        datas = input('Input Information..')
        datas = datas.split(' ')
        # id = input("Input Id...")
        # pwd = input("Input pwd...")
        # name = input("Input name...")
        # age = input("Input age...")
        dbutil.insert(id=datas[0].strip(),pwd=datas[1].strip(),name=datas[2].strip(),age=int(datas[3].strip()))
    elif menu=='s':
        id = input("Input Id...")
        users = dbutil.select(id=id)
        user = users[0]
        print("id : %s\npwd : %s\nname : %s\nage : %3d" % (user[0], user[1], user[2], user[3]))
    elif menu=='sa':
        users = dbutil.select()
        for u in users:
            print("id : %s\npwd : %s\nname : %s\nage : %3d\n"%(u[0],u[1],u[2],u[3]))
    else:
        print("Please Input i or s or sa or q")
print('end')