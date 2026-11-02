
def lettre_vers_nombre(c):
    return ord(c) - ord("A")


def nombre_vers_lettre(n):
    return chr(n + ord("A"))


print(lettre_vers_nombre("C"))
print(nombre_vers_lettre(2))