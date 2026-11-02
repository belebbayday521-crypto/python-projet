
for n in [200, 400, 800]:
    P = [1] * (n + 1)

    t1 = duree(evaluer_naif, P, 3)
    t2 = duree(evaluer, P, 3)

    print("Degre =", n)
    print("Naif =", t1)
    print("Horner =", t2)
    print("Rapport =", t1 / t2)