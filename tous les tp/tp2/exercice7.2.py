
def puissance_rapide(a, e, n):
    resultat = 1
    a = a % n

    while e > 0:
        if e % 2 == 1:
            resultat = (resultat * a) % n

        a = (a * a) % n
        e = e // 2

    return resultat

print(puissance_rapide(2, 10, 1000))