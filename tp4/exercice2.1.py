
def produit(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)

    C = []

    for i in range(n):
        ligne = []

        for j in range(m):
            s = 0

            for k in range(p):
                s = s + A[i][k] * B[k][j]

            ligne.append(s)

        C.append(ligne)

    return C


A = [[1, 2],
     [3, 4]]

I = [[1, 0],
     [0, 1]]

print(produit(A, I))