from math import gcd

def inverse_modulaire(a, n):
    if gcd(a, n) != 1:
        raise ValueError("Inverse inexistant")

    for x in range(n):
        if (a * x) % n == 1:
            return x


print(inverse_modulaire(5, 26))