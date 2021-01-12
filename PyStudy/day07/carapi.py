class Car:

    serial = 1000

    def __init__(self, id, name, fsize, cfsize):
        self.__id = id
        self.__name = name
        self.__fsize = fsize
        self.__cfsize = cfsize
        self.__serial = Car.serial
        Car.serial += 1

    def print(self):
        return self.__id, self.__name, self.__fsize, self.__cfsize

    def setCfSize(self, cfsize):
        self.__cfsize = cfsize