
def newton(P, depart, tolerance):
    D = deriver(P)
    x = depart

    while True:
        nouveau_x = x - evaluer(P, x) / evaluer(D, x)

        if abs(nouveau_x - x) < tolerance:
            return nouveau_x

        x = nouveau_x

P = [-5, -2, 0, 1]

print(newton(P, 2, 1e-10))