
import numpy as np
import matplotlib.pyplot as plt

def rotation(angle):
    c = np.cos(angle)
    s = np.sin(angle)

    return np.array([[c, -s],
                     [s, c]])


maison = np.array([
    [0, 0],
    [2, 0],
    [2, 1.5],
    [1, 2.5],
    [0, 1.5],
    [0, 0]
]).T

plt.figure(figsize=(5, 5))

plt.plot(maison[0], maison[1], label="Depart")

for angle in (np.pi / 6, np.pi / 3, np.pi / 2):
    image = rotation(angle) @ maison

    plt.plot(image[0], image[1],
             label=str(angle))

plt.axis("equal")
plt.grid()
plt.legend()
plt.show()