class Car:
    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1
    @classmethod
    def outcount(cls):
        print(cls.count)
    @staticmethod
    def hello():
        print("오늘도 안전운전하세요")

Car.hello()

pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()
print(Car.count)

class Date:
    def __init__(self, month):
        self.__month = month;

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if 1 <= month <= 12:
            self.__month = month

today = Date(8)
today.month = 15
print(today.month)