
def se_coupent(A, B, C, D):
    """
    Teste si deux segments se croisent.
    Les cas avec trois points alignes ne sont pas traites.
    """

    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)

    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)

    return o1 * o2 < 0 and o3 * o4 < 0


# Diagonales du carre
print(se_coupent(
    (0, 0), (1, 1),
    (0, 1), (1, 0)
))

# Deux segments paralleles
print(se_coupent(
    (0, 0), (2, 0),
    (0, 1), (2, 1)
))

# Deux segments alignes mais disjoints
print(se_coupent(
    (0, 0), (1, 0),
    (2, 0), (3, 0)
))