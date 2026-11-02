import math

def racines_naif(a, b, c):
    delta = b * b - 4 * a * c

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2

x1, x2 = racines_naif(1, -1e8, 1)

print(x1)
print(x2)
print(x1 * x2)