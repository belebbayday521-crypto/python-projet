import math

def vecteur(A, B):
    return (B[0] - A[0], B[1] - A[1])


def produit_scalaire(u, v):
    return u[0] * v[0] + u[1] * v[1]


def norme(u):
    return math.sqrt(u[0]**2 + u[1]**2)


def angle(u, v):
    ps = produit_scalaire(u, v)

    n1 = norme(u)
    n2 = norme(v)

    if n1 == 0 or n2 == 0:
        raise ValueError("Angle impossible avec un vecteur nul")

    cos_angle = ps / (n1 * n2)

    cos_angle = max(-1, min(1, cos_angle))

    return math.degrees(math.acos(cos_angle))


print(norme((3, 4)))
print(produit_scalaire((1, 2), (3, 4)))
print(angle((1, 0), (1, 1)))
print(angle((1, 0), (0, 1)))