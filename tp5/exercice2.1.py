
def lettre_vers_nombre(c):
    return ord(c) - ord("A")


def nombre_vers_lettre(n):
    return chr(n + ord("A"))


def chiffrer(texte, a, b):
    resultat = ""

    for c in texte:
        x = lettre_vers_nombre(c)

        y = (a * x + b) % 26

        resultat = resultat + nombre_vers_lettre(y)

    return resultat


print(chiffrer("ATTAQUEALAUBE", 5, 8))