print("start")
while True:
    data = input("input number[q:quit] : ")
    if data.lower() == 'q':
        print("exit")
        exit(1)
    elif data.isnumeric():
        result = int(data)
        print(result)
    else:
        print("invalid number type")

print("end")