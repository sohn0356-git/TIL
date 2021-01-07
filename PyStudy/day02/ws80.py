ko = input("Input Ko Score...?")
en = input("Input En Score...?")
si = input("Input Si Score...?")
ma = input("Input Ma Score...?")

if ko.isnumeric() and en.isnumeric() and si.isnumeric() and ma.isnumeric():
    ko = int(ko)
    en = int(en)
    si = int(si)
    ma = int(ma)
    sum = ko+en+si+ma
    avg = sum/4
    if avg>=90:
        print("A")
    elif avg>=80:
        print("B")
    elif avg>=70:
        print("C")
    elif avg>=60:
        print("D")
    else:
        print("F")