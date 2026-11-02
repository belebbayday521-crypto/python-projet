
P = [2, -2, 0, 1]
D = deriver(P)

x = 0

for i in range(10):
    nouveau_x = x - evaluer(P, x) / evaluer(D, x)

    print(nouveau_x)

    x = nouveau_x