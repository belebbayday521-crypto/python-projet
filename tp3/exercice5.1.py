
import matplotlib.pyplot as plt

P = [-5, -2, 0, 1]

xs = []

for i in range(-300, 301):
    xs.append(i / 100)

ys = []

for x in xs:
    ys.append(evaluer(P, x))

plt.plot(xs, ys)
plt.axhline(0)
plt.axvline(0)

plt.ylim(-20, 20)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Polynome")

plt.show()