
def determinant(u, v):
    return u[0] * v[1] - u[1] * v[0]


def distance_point_droite(P, A, B):
    AB = vecteur(A, B)
    AP = vecteur(A, P)

    return abs(determinant(AB, AP)) / norme(AB)


print(distance_point_droite((0, 0), (0, 4), (3, 0)))
print(distance_point_droite((2, 4), (0, 0), (5, 0)))
