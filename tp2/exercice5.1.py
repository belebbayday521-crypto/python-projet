
def facteurs(n):
    liste = []
    d = 2

    while n > 1:
        if n % d == 0:
            liste.append(d)
            n = n // d
        else:
            d = d + 1

    return liste

print(facteurs(360))
