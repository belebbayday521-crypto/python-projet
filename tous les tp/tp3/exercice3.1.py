def deriver(P):
    D = []

    for i in range(1, len(P)):
        D.append(i * P[i])

    return D

print(deriver([2, 3, 0, 5]))