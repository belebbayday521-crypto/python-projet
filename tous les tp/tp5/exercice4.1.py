from math import gcd

def inverse_modulaire(a, n):
    if gcd(a, n) != 1:
        raise ValueError("Inverse inexistant")

    for x in range(n):
        if (a * x) % n == 1:
            return x


def lettre_vers_nombre(c):
    return ord(c) - ord("A")


def nombre_vers_lettre(n):
    return chr(n + ord("A"))


def dechiffrer(texte, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Cle invalide")

    inv = inverse_modulaire(a, 26)

    resultat = ""

    for c in texte:
        y = lettre_vers_nombre(c)

        x = (inv * (y - b)) % 26

        resultat = resultat + nombre_vers_lettre(x)

    return resultat


m = "ATTAQUEALAUBE"

secret = chiffrer(m, 5, 8)

print(secret)
print(dechiffrer(secret, 5, 8))