class Account:                                   #class = 캡슐화, 연관된 정보를 묶어둠
    def __init__(self, accNo, balance, rate):    #constructor, 최초의 객체를 초기화(class)
        self.accNo = accNo;
        self.balance = balance;                  #balance = 예금잔액 표시
        self.rate = rate;                        #deposit = 입출금 동작 수행
    def __str__(self):
        return self.accNo+' '+str(self.balance)+' '+str(self.rate);
    def deposit(self, money):                    #inquire = 잔액을 조회하여 출력
        self.balance += money;
    def withdraw(self, money):
        self.balance -= money;
    def inquire(self):
        return self.balance;

def getAvg(accList):
    bsum = 0;
    rsum = 0.0;

    for acc in accList:
        bsum += acc.__balance;
        rsum += acc.rate;

    return(bsum / len(accList),(rsum / len(accList)));
