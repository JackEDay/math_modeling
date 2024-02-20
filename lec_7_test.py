import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def circle_move(R, vx0, vy0, t):
    x0 = vx0 * t
    y0 = vy0 * t
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

def animate(i):
    ball.set_data(circle_move(R=np.arange(0, 5, 0.1), vx0=0.01, vy0=0.01, t=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')

    edge = 3
    plt.axis('equal')

    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, 
                        animate,
                        frames=100,
                        interval=30
                        )
    
    ani.save('animation_test.gif')