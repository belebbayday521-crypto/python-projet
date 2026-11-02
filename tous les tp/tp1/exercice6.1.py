def vers_binaire(n):
    if n == 0:
        return "0"

    resultat = ""

    while n > 0:
        reste = n % 2
        resultat = str(reste) + resultat
        n = n // 2

    return resultat

print(vers_binaire(37))
print(vers_binaire(0))