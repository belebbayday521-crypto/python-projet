
from math import gcd

cles = []

for a in range(1, 26):
    if gcd(a, 26) == 1:
        cles.append(a)

print(cles)
print(len(cles))