class Account:
    def __init__(self, accNo, balance,rate):
        self.accNo = accNo
        self.balance = balance
        self.rate = rate
    def deposit(self,money):
        self.balance += money
    def withdraw(self,money):
        self.balance -= money
    def inquire(self):
        self.balance

account = Account('ss',100,5)