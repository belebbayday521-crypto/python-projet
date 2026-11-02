
import random

def indice_coincidence(texte):
    N = len(texte)

    if N < 2:
        return 0

    frequences = [0] * 26

    for c in texte:
        x = lettre_vers_nombre(c)
        frequences[x] = frequences[x] + 1

    somme = 0

    for n in frequences:
        somme = somme + n * (n - 1)

    return somme / (N * (N - 1))


texte_long = nettoyer(
    "Le chiffrement affine est un exemple simple "
    "de cryptographie classique utilise pour comprendre "
    "les mathematiques et les nombres."
)

secret_long = chiffrer(texte_long, 5, 8)

texte_aleatoire = ""

for i in range(len(texte_long)):
    x = random.randint(0, 25)
    texte_aleatoire = texte_aleatoire + nombre_vers_lettre(x)

print("Clair :", indice_coincidence(texte_long))
print("Chiffre :", indice_coincidence(secret_long))
print("Aleatoire :", indice_coincidence(texte_aleatoire))