
def transposee(A):
    n = len(A)
    m = len(A[0])

    T = []

    for j in range(m):
        ligne = []
        for i in range(n):
            ligne.append(A[i][j])
        T.append(ligne)

    return T


A = [[1, 2, 3],
     [4, 5, 6]]

print(transposee(A))