
def dichotomie(f, a, b, tolerance):
    while b - a > tolerance:
        m = (a + b) / 2

        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m

    return (a + b) / 2

def f(x):
    return x**3 - 2*x - 5

print(dichotomie(f, 2, 3, 1e-10))