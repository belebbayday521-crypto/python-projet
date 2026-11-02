
import numpy as np
import random

n = 50

A = [[random.random() for j in range(n)] for i in range(n)]
b = [random.random() for i in range(n)]

x1 = resoudre(A, b)

x2 = np.linalg.solve(np.array(A), np.array(b))

print("Solution Gauss :", x1)
print("Solution numpy :", x2)

erreur = np.max(np.abs(np.array(x1) - x2))

print("Erreur :", erreur)