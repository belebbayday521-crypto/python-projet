import math

def f1(x):
    return x**2 - 2

def df1(x):
    return 2*x

def f2(x):
    return x**3 - x - 2

def df2(x):
    return 3*x**2 - 1

def f3(x):
    return math.cos(x) - x

def df3(x):
    return -math.sin(x) - 1


def dichotomie(f, a, b, epsilon=0.000001, max_iter=100):
    if f(a) * f(b) > 0:
        return None, 0, False

    iteration = 0
    while (b - a) / 2 > epsilon and iteration < max_iter:
        milieu = (a + b) / 2

        if f(milieu) == 0:
            return milieu, iteration + 1, True

        if f(a) * f(milieu) < 0:
            b = milieu
        else:
            a = milieu

        iteration += 1

    return (a + b) / 2, iteration, True


def newton(f, df, x_depart, epsilon=0.000001, max_iter=100):
    x = x_depart
    anciennes_valeurs = []

    for iteration in range(max_iter):
        valeur = f(x)
        derivee = df(x)

        if abs(valeur) < epsilon:
            return x, iteration, True, "Convergence"

        if abs(derivee) < 0.0000000001:
            return x, iteration, False, "Derivee presque nulle"

        nouveau_x = x - valeur / derivee

        for ancienne in anciennes_valeurs:
            if abs(nouveau_x - ancienne) < epsilon:
                return nouveau_x, iteration + 1, False, "Cycle possible"

        anciennes_valeurs.append(x)

        if abs(nouveau_x) > 1000000:
            return nouveau_x, iteration + 1, False, "Divergence possible"

        x = nouveau_x

    return x, max_iter, False, "Maximum d'iterations atteint"


def solveur_automatique(f, df, x_depart, a, b, epsilon=0.000001):
    print("\n Newton")
    resultat, nb, reussi, message = newton(f, df, x_depart, epsilon)
    print("Resultat :", resultat)
    print("Iterations :", nb)
    print("Etat :", message)

    if reussi:
        return resultat, "Newton"

    print("\n Newton n'a pas converge. Essai de la dichotomie...")
    resultat, nb, possible = dichotomie(f, a, b, epsilon)

    if possible:
        print("Resultat dichotomie :", resultat)
        print("Iterations :", nb)
        return resultat, "Dichotomie"

    print("Dichotomie impossible sur cet intervalle.")
    return None, "Aucune methode n'a reussi"


def comparer_methodes(f, df, x_depart, a, b):
    rn, inn, okn, msg = newton(f, df, x_depart)
    rd, ind, okd = dichotomie(f, a, b)

    print("\n Comparaison")
    if okn:
        print("Newton :", rn, "| iterations :", inn)
    else:
        print("Newton n'a pas converge :", msg)

    if okd:
        print("Dichotomie :", rd, "| iterations :", ind)
    else:
        print("Dichotomie impossible avec cet intervalle.")


def dessiner_fonction(f, a, b, titre):
    try:
        import matplotlib.pyplot as plt

        valeurs_x = []
        valeurs_y = []
        pas = (b - a) / 200
        x = a

        while x <= b:
            valeurs_x.append(x)
            valeurs_y.append(f(x))
            x += pas

        plt.plot(valeurs_x, valeurs_y, label="f(x)")
        plt.axhline(0)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(titre)
        plt.grid()
        plt.legend()
        plt.show()
    except ImportError:
        print("Installer le matplotlib pour afficher le graphique.")


def main():
    print("SOLVEUR AUTOMATIQUE D'EQUATIONS")
    print("1 : f(x) = x^2 - 2")
    print("2 : f(x) = x^3 - x - 2")
    print("3 : f(x) = cos(x) - x")

    choix = input("Choix (1, 2 ou 3) : ")

    if choix == "1":
        f, df, a, b, x0 = f1, df1, 1, 2, 1.5
        titre = "f(x) = x^2 - 2"
    elif choix == "2":
        f, df, a, b, x0 = f2, df2, 1, 2, 1.5
        titre = "f(x) = x^3 - x - 2"
    elif choix == "3":
        f, df, a, b, x0 = f3, df3, 0, 1, 0.5
        titre = "f(x) = cos(x) - x"
    else:
        print("Choix incorrect.")
        return

    print("Intervalle :", a, "a", b)
    print("Point de depart Newton :", x0)
    solveur_automatique(f, df, x0, a, b)
    comparer_methodes(f, df, x0, a, b)
    dessiner_fonction(f, a, b, titre)


if __name__ == "__main__":
    main()
