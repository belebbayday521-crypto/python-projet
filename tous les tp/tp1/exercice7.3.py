from fractions import Fraction

s = Fraction(0)

for i in range(1000):
    s = s + Fraction(1, 10)

print(s)
print(s == 100)

a = Fraction(1, 10)
b = Fraction(2, 10)
c = Fraction(3, 10)

print(a + b == c)