
def somme(P, Q):
    R = []

    n = max(len(P), len(Q))

    for i in range(n):
        a = 0
        b = 0

        if i < len(P):
            a = P[i]

        if i < len(Q):
            b = Q[i]

        R.append(a + b)

    return R

print(somme([1, 1], [1, 1]))
print(somme([1, 2, 3], [4, 5]))