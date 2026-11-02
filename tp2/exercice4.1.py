
def crible(limite):
    tableau = [True] * (limite + 1)

    tableau[0] = False

    if limite >= 1:
        tableau[1] = False

    d = 2

    while d * d <= limite:

        if tableau[d]:
            for multiple in range(d * d, limite + 1, d):
                tableau[multiple] = False

        d = d + 1

    liste = []

    for n in range(limite + 1):
        if tableau[n]:
            liste.append(n)

    return liste

import time

debut = time.perf_counter()
liste = crible(100000)
fin = time.perf_counter()

print("Nombre de premiers =", len(liste))
print("Temps =", fin - debut)
