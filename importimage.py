import matplotlib.pyplot as plt
import numpy as np

image = plt.imread('horsead.jpg')
fig, ax = plt.subplots()

ax.imshow(image, extent=[0, 1000, 0, 250])

plt.ylim(0, 350)

plt.savefig("HOrshead.png")

