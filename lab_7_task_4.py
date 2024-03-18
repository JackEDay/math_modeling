import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def animation(x, y, C, D, n):

    xdata1, ydata1 = [], []
    xdata1.append(x)
    ydata1.append(y)

    def animate(i):
        xdata1.append(xdata1[i]**2 - ydata1[i]**2 + C)
        ydata1.append(2 * xdata1[i] * ydata1[i] + D)
        kill.set_data(xdata1, ydata1)
        return kill,

    if __name__ == '__main__':
        plt.axis('equal')
        fig, ax = plt.subplots()
        kill, = plt.plot([], [], 'o', color='r', label='Ball')
        edge = 1

        ax.set_xlim(-edge, edge)
        ax.set_ylim(-edge, edge)

        ani = FuncAnimation(fig, 
                            animate,
                            frames=50,
                            interval=200
                            )
        ani.save('Lab_7_task_4.gif')

animation(0.1, 0.1, 0.3, 0.33, 40)