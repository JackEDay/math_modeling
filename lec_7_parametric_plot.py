import matplotlib.pyplot as plt
import numpy as np

def circle_plot(R):
    alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)

    x = R * np.cos(alpha)
    y = R * np.sin(alpha)

    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.grid()
    plt.savefig('Parametric_plot.png')

if __name__ == '__main__':
    circle_plot(3)