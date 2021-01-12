from decimal import Decimal
from fractions import Fraction
n = Decimal('0.1')
sum = 0
for i in range(10):
    sum += n
print(sum)
print(Fraction(1,3)+Fraction(1,6)+Fraction(1,2))
print(Fraction(1,3)+Fraction(1,4) + 0.0)