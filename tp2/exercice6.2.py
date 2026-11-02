
compteur = {}

def fibonacci_recursif(n):
    if n not in compteur:
        compteur[n] = 0

    compteur[n] = compteur[n] + 1

    if n < 2:
        return n

    return fibonacci_recursif(n - 1) + fibonacci_recursif(n - 2)

print(fibonacci_recursif(30))
print("F(1) =", compteur[1])
print("Total =", sum(compteur.values()))