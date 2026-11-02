
def intersection(A, B, C, D):
    if not se_coupent(A, B, C, D):
        return None

    AB = vecteur(A, B)
    CD = vecteur(C, D)
    AC = vecteur(A, C)

    denominateur = determinant(AB, CD)

    t = determinant(AC, CD) / denominateur

    x = A[0] + t * AB[0]
    y = A[1] + t * AB[1]

    return (x, y)


print(intersection(
    (0, 0), (2, 2),
    (0, 2), (2, 0)
))