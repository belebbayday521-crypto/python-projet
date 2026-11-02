
def pgcd(a, b):
    while b != 0:
        reste = a % b
        a = b
        b = reste

    return a

print(pgcd(1071, 462))