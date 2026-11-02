import math

def heron(a):
    x = a

    while True:
        nouveau_x = (x + a / x) / 2

        if math.isclose(x, nouveau_x, abs_tol=1e-12):
            return nouveau_x

        x = nouveau_x

resultat = heron(2)

print(resultat)
print(math.sqrt(2))
print(abs(resultat - math.sqrt(2)))