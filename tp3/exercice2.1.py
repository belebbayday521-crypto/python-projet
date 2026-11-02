
def evaluer(P, x):
    resultat = 0

    for i in range(len(P) - 1, -1, -1):
        resultat = resultat * x + P[i]

    return resultat

P = [2, 3, 0, 5]

print(evaluer(P, 2))
print(evaluer_naif(P, 2))