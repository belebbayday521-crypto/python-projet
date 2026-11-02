
import random
import time

def matrice_aleatoire(n):
    return [[random.random() for j in range(n)] for i in range(n)]

for n in [40, 80, 120]:
    A = matrice_aleatoire(n)
    B = matrice_aleatoire(n)

    debut = time.time()
    C = produit(A, B)
    fin = time.time()

    print(n, fin - debut)