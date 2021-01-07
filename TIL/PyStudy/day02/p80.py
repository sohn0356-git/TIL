print("start")
a = input("Input Number ..?")
if a.isnumeric():
    a = int(a)
    if a>10:
        print("Big")
    elif a>5:
        print("Normal")
    else:
        print("Small")

print("end")