
def produit_poly(P, Q):
    R = [0] * (len(P) + len(Q) - 1)

    for i in range(len(P)):
        for j in range(len(Q)):
            R[i + j] = R[i + j] + P[i] * Q[j]

    return R

print(produit_poly([1, 1], [1, 1]))
print(produit_poly([-1, 1], [1, 1]))