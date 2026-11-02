
def evaluer_naif(P, x):
    resultat = 0

    for i in range(len(P)):
        resultat = resultat + P[i] * x**i

    return resultat

P = [2, 3, 0, 5]

print(evaluer_naif(P, 2))