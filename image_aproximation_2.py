import matplotlib.pyplot as plt
import numpy as np

image = plt.imread('Barnard_68.jpg')
fig, ax = plt.subplots()

ax.imshow(image)

t = np.linspace(np.pi/2, np.pi*3/2, 100)
x = 75 + 10 * np.cos(t)
y = 195 - 10 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='b')

plt.savefig("Barnard_apx.png")