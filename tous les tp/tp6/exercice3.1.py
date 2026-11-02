def se_coupent(A, B, C, D):

    o1 = orientation(A, B, C)
    o2 = orientation(A, B, D)

    o3 = orientation(C, D, A)
    o4 = orientation(C, D, B)

    return o1 * o2 < 0 and o3 * o4 < 0


print(se_coupent(
    (0, 0), (1, 1),
    (0, 1), (1, 0)
))

print(se_coupent(
    (0, 0), (2, 0),
    (0, 1), (2, 1)
))

print(se_coupent(
    (0, 0), (1, 0),
    (2, 0), (3, 0)
))