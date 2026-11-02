
def euclide_etendu(a, b):
    if b == 0:
        return a, 1, 0

    g, u, v = euclide_etendu(b, a % b)

    return g, v, u - (a // b) * v

print(euclide_etendu(1071, 462))