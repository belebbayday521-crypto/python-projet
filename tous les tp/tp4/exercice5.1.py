import numpy as np

def hilbert(n):
    return np.array([
        [1.0 / (i + j + 1) for j in range(n)]
        for i in range(n)
    ])

n = 12

H = hilbert(n)
x_vrai = np.ones(n)

b = H @ x_vrai

x_solve = np.linalg.solve(H, b)
x_inverse = np.linalg.inv(H) @ b

print("Erreur solve :", np.max(np.abs(x_solve - x_vrai)))
print("Erreur inverse :", np.max(np.abs(x_inverse - x_vrai)))
print("Conditionnement :", np.linalg.cond(H))