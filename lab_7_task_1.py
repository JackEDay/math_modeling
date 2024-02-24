import matplotlib.pyplot as plt
import numpy as np

def draw_cycloid(a):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)
    x = a * (t - np.sin(t))
    y = a * (1 - np.cos(t))

    plt.axis('equal')
    plt.grid()
    plt.plot(x, y)
    plt.savefig('task_cycloid.png')

def draw_astroid(R, t):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3

    plt.axis('equal')
    plt.grid()
    plt.plot(x, y)
    plt.savefig('task_astroid.png')

#draw_cycloid(1)
draw_astroid(2, 1)