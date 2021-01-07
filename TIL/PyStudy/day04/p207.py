# CART 구현
#1. 상품이름, 가격, 개수
#2. 위의 항목을 입력 받아서 CART에 넣는다.

products = []

def remove_product(product):
    for p in products:
        if p[0]==product:
            products.remove(p)
            break

def insert_product():
    product = input("상품이름, 가격, 개수를 입력하세요 : ").split(' ')
    if len(product) == 3 and product[1].isdecimal() and product[2].isdecimal():
        products.append(product)

def view_product():
    ptotal = 0
    ctotal = 0
    for p in products:
        print("상품명 : %s, 가격 : %d, 개수 : %d" % (p[0], int(p[1]), int(p[2])))
        ptotal += int(p[1])
        ctotal += int(p[2])
    print('Total : %d %d'%(ptotal,ctotal))
print('start')


while True:
    menu = input("i. cart에 넣기, v. cart 정보 보기, r. 지우기, q. 나가기 ").lower()
    if menu=='i':
        insert_product()
    elif menu=='v':
        view_product()
    elif menu=='r':
        product = input('지울 상품명을 입력하세요 : ')
        remove_product(product)
    elif menu=='q':
        print("exit")
        break

print('end')

