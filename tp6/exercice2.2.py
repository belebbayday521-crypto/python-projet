
def aire(polygone):
    n = len(polygone)
    somme = 0

    for i in range(n):
        j = (i + 1) % n

        x1 = polygone[i][0]
        y1 = polygone[i][1]

        x2 = polygone[j][0]
        y2 = polygone[j][1]

        somme = somme + x1 * y2 - y1 * x2

    return abs(somme) / 2


carre = [(0, 0), (1, 0), (1, 1), (0, 1)]

triangle = [(0, 0), (4, 0), (4, 3)]

maison = [(0, 0), (2, 0), (2, 1.5),
          (1, 2.5), (0, 1.5)]

print(aire(carre))
print(aire(triangle))
print(aire(maison))