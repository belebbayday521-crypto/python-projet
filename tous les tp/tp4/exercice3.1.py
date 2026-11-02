
import numpy as np
import random
import time

n = 120

A = [[random.random() for j in range(n)] for i in range(n)]
B = [[random.random() for j in range(n)] for i in range(n)]

debut = time.time()
C = produit(A, B)
fin = time.time()

temps_python = fin - debut

A_np = np.array(A)
B_np = np.array(B)

debut = time.time()
C_np = A_np @ B_np
fin = time.time()

temps_numpy = fin - debut

print("Temps Python :", temps_python)
print("Temps numpy :", temps_numpy)
print("Rapport :", temps_python / temps_numpy)