
def newton_compteur(P, depart, tolerance):
    D = deriver(P)
    x = depart
    compteur = 0

    while True:
        nouveau_x = x - evaluer(P, x) / evaluer(D, x)
        compteur = compteur + 1

        if abs(nouveau_x - x) < tolerance:
            return nouveau_x, compteur

        x = nouveau_x

P = [-5, -2, 0, 1]

print(newton_compteur(P, 2, 1e-10))
print(newton_compteur(P, 0, 1e-10))