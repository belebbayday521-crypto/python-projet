def dedans(P, polygone):
    x = P[0]
    y = P[1]

    n = len(polygone)
    compteur = 0

    for i in range(n):
        j = (i + 1) % n

        x1 = polygone[i][0]
        y1 = polygone[i][1]

        x2 = polygone[j][0]
        y2 = polygone[j][1]

        if (y1 > y) != (y2 > y):

            x_inter = x1 + (y - y1) * (x2 - x1) / (y2 - y1)

            if x_inter > x:
                compteur = compteur + 1

    return compteur % 2 == 1


maison = [(0, 0), (2, 0), (2, 1.5),
          (1, 2.5), (0, 1.5)]

print(dedans((1, 1), maison))
print(dedans((1, 2.4), maison))
print(dedans((3, 1), maison))
print(dedans((0.2, 2.2), maison))