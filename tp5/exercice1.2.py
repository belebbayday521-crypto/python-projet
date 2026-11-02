
import unicodedata

def nettoyer(texte):
    texte = texte.upper()

    # Suppression des accents
    texte = unicodedata.normalize("NFD", texte)

    resultat = ""

    for c in texte:
        if "A" <= c <= "Z":
            resultat = resultat + c

    return resultat


print(nettoyer("Été, à Paris !"))