import math

def presque_egaux(a, b):
    return math.isclose(a, b)

print(presque_egaux(0.1 + 0.2, 0.3))