
def pgcd_naif(a, b):
    resultat = 1

    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            resultat = d

    return resultat

print(pgcd_naif(1071, 462))