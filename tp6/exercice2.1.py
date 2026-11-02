
def orientation(A, B, C):
    AB = vecteur(A, B)
    AC = vecteur(A, C)

    d = determinant(AB, AC)

    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0


print(orientation((0, 0), (1, 0), (1, 1)))
print(orientation((0, 0), (1, 0), (1, -1)))
print(orientation((0, 0), (1, 1), (2, 2)))