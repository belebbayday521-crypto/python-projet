
def lettre_plus_frequente(texte):
    frequences = [0] * 26

    for c in texte:
        x = lettre_vers_nombre(c)
        frequences[x] = frequences[x] + 1

    maximum = 0
    lettre = 0

    for i in range(26):
        if frequences[i] > maximum:
            maximum = frequences[i]
            lettre = i

    return lettre


def casser_frequences(secret):
    y = lettre_plus_frequente(secret)

    resultats = []

    # E correspond au nombre 4
    for a in range(1, 26):
        if gcd(a, 26) == 1:

            b = (y - 4 * a) % 26

            texte = dechiffrer(secret, a, b)

            resultats.append((a, b, texte))

    return resultats


secret = chiffrer("ATTAQUEALAUBE", 5, 8)

for a, b, texte in casser_frequences(secret):
    print(a, b, texte)