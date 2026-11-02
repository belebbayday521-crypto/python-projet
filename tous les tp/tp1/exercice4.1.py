def nombre_de_chiffres(n):
    compteur = 0

    while n > 0:
        n = n // 10
        compteur = compteur + 1

    return compteur

print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))