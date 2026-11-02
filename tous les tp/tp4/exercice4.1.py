
def resoudre(A, b):
    n = len(A)

    M = [A[i][:] for i in range(n)]
    v = b[:]

    for k in range(n):

        pivot = k

        for i in range(k + 1, n):
            if abs(M[i][k]) > abs(M[pivot][k]):
                pivot = i

        M[k], M[pivot] = M[pivot], M[k]
        v[k], v[pivot] = v[pivot], v[k]

        if M[k][k] == 0:
            raise ValueError("Matrice singuliere")

        for i in range(k + 1, n):
            facteur = M[i][k] / M[k][k]

            for j in range(k, n):
                M[i][j] = M[i][j] - facteur * M[k][j]

            v[i] = v[i] - facteur * v[k]

    x = [0] * n

    for i in range(n - 1, -1, -1):
        s = 0

        for j in range(i + 1, n):
            s = s + M[i][j] * x[j]

        x[i] = (v[i] - s) / M[i][i]

    return x


A = [[1, 2, 2],
     [1, 3, -2],
     [3, 5, 8]]

b = [2, -1, 8]

x = resoudre(A, b)

print(x)