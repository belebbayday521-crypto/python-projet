def indice_moyen_colonnes(secret, L):
    somme = 0

    for i in range(L):
        colonne = ""

        for j in range(i, len(secret), L):
            colonne = colonne + secret[j]

        somme = somme + indice_coincidence(colonne)

    return somme / L


for L in range(1, 8):
    print(L, indice_moyen_colonnes(secret_vigenere, L))