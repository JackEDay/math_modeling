import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fix, ax = plt.subplots()

x = [1, 2, 3]
y = [7, 9, 7]
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(np.pi/2+np.pi/6 , np.pi/2-np.pi/6, 100)
x = 4 + 2 * np.cos(t)
y = 5.25 + 2 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

x = [5, 6, 7]
y = [7, 9, 7]
ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(np.pi*2 , np.pi, 100)
x = 4 + 3 * np.cos(t)
y = 7 + 5 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

#glaz1
t = np.linspace(np.pi/3 , np.pi*2/3, 100)
x = 2.5 + 2 * np.cos(t)
y = 4.25 + 2 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')
t = np.linspace(-np.pi*2/3 , -np.pi/3, 100)
x = 2.5 + 2 * np.cos(t)
y = 7.68 + 2 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')
#glaz2
t = np.linspace(np.pi/3 , np.pi*2/3, 100)
x = 5.25 + 2 * np.cos(t)
y = 4.25 + 2 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')
t = np.linspace(-np.pi*2/3 , -np.pi/3, 100)
x = 5.25 + 2 * np.cos(t)
y = 7.68 + 2 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

#nose
x = [3, 4, 5, 3]
y = [5, 4, 5, 5]
ax.plot(x, y, '-', lw=2, color='k')

#mouth
t = np.linspace(-(np.pi/2-np.pi/6) , -(np.pi/2+np.pi/6), 100)
x = 4 + 2 * np.cos(t)
y = 5.25 + 2 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='k')

plt.axis('equal')

plt.savefig('Cool.png')