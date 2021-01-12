class Human:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return "이름 %s, 나이 %d" % (self.name, self.age)

    def __repr__(self):
        return "Human(" + str(self.age) + ",'" + self.name + "')"

kim = Human(29, '김상형')
print(kim)
kimexp = repr(kim)
print(kimexp)
kimcopy = eval(kimexp)
print(kimcopy)