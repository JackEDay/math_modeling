import matplotlib.pyplot as plt
import numpy as np


def draw(a):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)
    x = a * (t - np.sin(t))
    y = a * (1 - np.cos(t))

    plt.axis('equal')
    plt.grid()
    plt.plot(x, y)
    plt.savefig('task_1.png')

draw(1)