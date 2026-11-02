def vigenere(texte, cle):
    resultat = ""

    for i in range(len(texte)):
        x = lettre_vers_nombre(texte[i])

        c = cle[i % len(cle)]
        y = lettre_vers_nombre(c)

        z = (x + y) % 26

        resultat = resultat + nombre_vers_lettre(z)

    return resultat


secret_vigenere = vigenere(texte_long, "CLE")

print(secret_vigenere)
print(indice_coincidence(secret_vigenere))