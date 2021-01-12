class Human:

    def __init__(self, name, age):
        self.__name = name
        if age <= 0:
            self.__age = -1
        else:
            self.__age = age

    def __str__(self):
        return self.__name + ' ' + str(self.__age)

    def print(self):
        return self.__name, self.__age

    def getAge(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

class Student(Human):

    def __init__(self, name, age, major):
        super().__init__(name,age)
        self.__major = major

    def print(self):
        return super().print() + (self.__major,)
