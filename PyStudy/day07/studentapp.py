import studentapi
from studentapi import *

human = Human('james',20)
print(human)
print("%s %d" % human.print())
print(type(human.print()))
student = Student('james',20,'chemistry')
print("%s %d %s" % student.print())