from bankapi import Account

acc1 = Account('1111',10000,4.5)
print('잔액정보 %d' % (acc1.inquire()))
acc1.deposit(5000)
print('잔액정보 %d' % acc1.inquire())

accList = []
accList.append(Account('1111',10000,3.5))
accList.append(Account('2222',10000,3.6))
accList.append(Account('3333',10000,3.7))
accList.append(Account('4444',10000,3.8))
accList.append(Account('5555',10000,3.9))

for acc in accList:
    print(acc)
    # print(acc.inquire())

# 잔액 평균과 금리 평균을 구하시오
Account.print_avr()