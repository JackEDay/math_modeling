import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

e = 2.71828
xdata1, ydata1 = [], []
xdata2, ydata2 = [], []

def animate(alpha):
    xdata1.append(np.sin(alpha) * (e**np.cos(alpha)- 2*np.cos(4*alpha) + (np.sin(alpha/12))**5))
    ydata1.append(np.cos(alpha) * (e**np.cos(alpha)- 2*np.cos(4*alpha) + (np.sin(alpha/12))**5))
    butter.set_data(xdata1, ydata1)
    return butter,

def update(beta):
    xdata2.append(16*(np.sin(beta))**3)
    ydata2.append(13*np.cos(beta) - 3*np.cos(2*beta) - 2*np.cos(3*beta) - 4*np.cos(4*beta))
    heart.set_data(xdata2, ydata2)
    return heart,

if __name__ == '__main__':
    plt.axis('equal')
    fig, ax = plt.subplots()

    # butter, = plt.plot([], [], 'o', color='r', label='Butterfly')
    # edge = 5
    # ax.set_xlim(-edge, edge)
    # ax.set_ylim(-edge, edge)
    # ani = FuncAnimation(fig, 
    #                     animate,
    #                     frames=np.arange(0, 12*np.pi, 0.1),
    #                     interval=30
    #                     )
    # ani.save('Lab_7_Butterfly.gif')

    heart, = plt.plot([], [], 'o', color='r', label='Heart')
    edge = 20
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    ani = FuncAnimation(fig, 
                        update,
                        frames=np.arange(0, 2*np.pi, 0.05),
                        interval=30
                        )
    ani.save('Lab_7_Heart.gif')