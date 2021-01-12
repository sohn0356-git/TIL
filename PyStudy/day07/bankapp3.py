from bankapi import Account
import bankapi

acc = Account('1111',10000,3.4)
print(acc)
try:
    acc.deposit(-15000)
    print(acc)
except Exception as e:
    print('Error 발생!', e)

