import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def planet(R, angle_vel, t):
    alpha = angle_vel * np.pi / 180 * t
    x = R * np.cos(alpha)
    y = R * np.sin(alpha) * 0.8
    return x, y

def animate(i):
    mercury.set_data(planet(R=0.4, angle_vel=3, t=i))
    venus.set_data(planet(R=0.8, angle_vel=2, t=i))
    mars.set_data(planet(R=1.2, angle_vel=2.3, t=i))
    earth.set_data(planet(R=1.6, angle_vel=1, t=i))
    
    ax.set_title(f'Day on Earth: {i}')

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plt.grid()
    plt.plot([0], [0], 'o', ms=12, color='orange')
    mercury, = plt.plot([], [], 'o', color='brown')
    venus, = plt.plot([], [], 'o', color='darkgoldenrod')
    mars, = plt.plot([], [], 'o', color='chocolate')
    earth, = plt.plot([], [], 'o', color='mediumblue')

    edge = 3

    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, 
                        animate,
                        frames=360,
                        interval=30
                        )
    ani.save('Project.gif')