class Account:
    bsum = 0
    rsum = 0
    count = 0
    def __init__(self, accNo, balance,rate):
        self.accNo = accNo
        self.__balance = balance
        self.rate = rate
        Account.bsum += balance
        Account.rsum += rate
        Account.count += 1
    def getRateMoeny(self):
        return self.__balance * self.rate
    def __str__(self):
        return self.accNo + ' ' + str(self.__balance) + ' ' + str(self.rate) + str(self.getRateMoeny())
    def deposit(self,money):
        if money <= 0:
            raise MinusError
        self.__balance += money
    def withdraw(self,money):
        if self.__balance<money:
            raise NotEnoughError
        self.__balance -= money
    def inquire(self):
        return self.__balance

    @classmethod
    def print_avr(cls):
        print("잔액 평균 : %.2f, 금리 평균 : %.2f"%(Account.bsum/Account.count,Account.rsum/Account.count))

class MinusError(Exception):
    """ Inappropriate argument value (of correct type). """
    def __init__(self): # real signature unknown
        super().__init__('입력 금액이 잘못되었습니다.')


class NotEnoughError(Exception):
    """ Inappropriate argument value (of correct type). """
    def __init__(self): # real signature unknown
        super().__init__('잔고보다 많은 돈을 출력하셨습니다.')
