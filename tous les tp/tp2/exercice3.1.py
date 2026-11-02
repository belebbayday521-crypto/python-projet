
import time

def duree(fonction, argument):
    debut = time.perf_counter()
    fonction(argument)
    fin = time.perf_counter()

    return fin - debut

nombres = [10007, 100003, 1000003]

for n in nombres:
    t1 = duree(est_premier_naif, n)
    t2 = duree(est_premier, n)

    print("n =", n)
    print("Naif =", t1)
    print("Optimise =", t2)
