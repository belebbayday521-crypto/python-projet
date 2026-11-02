
import time

def duree(fonction, P, x):
    debut = time.perf_counter()
    fonction(P, x)
    fin = time.perf_counter()

    return fin - debut

for n in [1000, 5000, 20000]:
    P = [1] * (n + 1)

    t1 = duree(evaluer_naif, P, 1.0001)
    t2 = duree(evaluer, P, 1.0001)

    print("Degre =", n)
    print("Naif =", t1)
    print("Horner =", t2)
    print("Rapport =", t1 / t2)
