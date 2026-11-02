
def toutes_les_clefs(secret):
    resultats = []

    for a in range(1, 26):
        if gcd(a, 26) == 1:

            for b in range(26):
                texte = dechiffrer(secret, a, b)

                resultats.append((a, b, texte))

    return resultats


secret = chiffrer("ATTAQUEALAUBE", 5, 8)

resultats = toutes_les_clefs(secret)

print("Nombre de clés :", len(resultats))

for a, b, texte in resultats:
    print(a, b, texte)