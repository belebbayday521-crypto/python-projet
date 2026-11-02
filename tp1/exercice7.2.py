import math

def racines(a, b, c):
    delta = b * b - 4 * a * c

    q = -0.5 * (b + math.copysign(math.sqrt(delta), b))

    x1 = q / a
    x2 = c / q

    return x1, x2

x1, x2 = racines(1, -1e8, 1)

print(x1)
print(x2)
print(x1 * x2)