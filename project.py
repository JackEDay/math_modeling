import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import warnings
import matplotlib
warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)

def planet(R, vel, t):
    alpha = vel * np.pi / 180 * t
    x = R * np.cos(alpha)
    y = R * np.sin(alpha) * 0.8
    return x, y

def animate(i):
    mercury.set_data(planet(R=2.1, vel=4.14772, t=i))    #Year = 88 days
    venus.set_data(planet(R=3.6, vel=1.62222, t=i))      #Year = 225 days
    earth.set_data(planet(R=5.5, vel=1, t=i))            #Year = 365 days
    mars.set_data(planet(R=7, vel=0.53129, t=i))         #Year = 687 days
    jupiter.set_data(planet(R=8.5, vel=0.08423, t=i))    #Year = 4333 days
    saturn.set_data(planet(R=9.8, vel=0.03392, t=i))     #Year = 10 759 days
    uranus.set_data(planet(R=11, vel=0.01189, t=i))      #Year = 30 687 days    
    neptune.set_data(planet(R=12, vel=0.00606, t=i))     #Year = 60 190 days
    moon.set_data(moonplt(R=1.2, vel=365, t=i))

    
    ax.set_title(f'Day on Earth: {i}')

def moonplt(R, vel, t):
    x0, y0 = (planet(R=5.5, vel=1, t=t))
    alpha = vel * np.pi / 180 * t
    x = x0 + R*np.cos(alpha) * 0.8
    y = y0 + R*np.sin(alpha) * 0.8
    return x, y

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plt.grid()
    plt.plot([0], [0], 'o', ms=29, color='orange')
    mercury, = plt.plot([], [], 'o', ms=3, color='brown')
    venus, = plt.plot([], [], 'o', ms=5, color='darkgoldenrod')
    mars, = plt.plot([], [], 'o', ms=4, color='chocolate')
    earth, = plt.plot([], [], 'o', color='mediumblue')
    jupiter, = plt.plot([], [], 'o', ms=14, color='sienna')
    saturn, = plt.plot([], [], 'o', ms= 12, color='bisque')
    uranus, = plt.plot([], [], 'o', ms=10.7, color='aquamarine')
    neptune, = plt.plot([], [], 'o', ms=10, color='royalblue')
    moon, = plt.plot([], [], 'o', ms=3, color='grey')

    edge = 12

    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, 
                        animate,
                        frames=999,
                        interval=20
                        )
    ani.save('Project_limit.gif')
