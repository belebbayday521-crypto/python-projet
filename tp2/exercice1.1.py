
def diviseurs(n):
    liste = []

    for d in range(1, n + 1):
        if n % d == 0:
            liste.append(d)

    return liste

print(diviseurs(28))
