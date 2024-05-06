import matplotlib.pyplot as plt
import numpy as np

image = plt.imread('horsead.jpg')
fig, ax = plt.subplots()

ax.imshow(image)

t = np.linspace(0, np.pi, 100)
x = 50 + 47 * np.cos(t)
y = 290 - 10 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi/2, np.pi*7/6, 100)
x = 138 + 47 * np.cos(t)
y = 275 - 30 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

x = [140, 164]
y = [246, 115]
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(-(np.pi*5/6), -np.pi/14, 100)
x = 110 + 55 * np.cos(t)
y = 105 - 45 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

x = [64, 90]
y = [126, 108]
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(-(np.pi*2/3), np.pi/6, 100)
x = 103 + 25 * np.cos(t)
y = 84 - 28 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

x = [126, 151]
y = [69, 43]
ax.plot(x, y, '-', lw=2, color='w')

x = [151, 210]
y = [43, 72]
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi*4/7, np.pi/8, 100)
x = 228 + 70 * np.cos(t)
y = 220 - 150 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

x = [293, 270]
y = [160, 285]
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi/2, np.pi, 100)
x = 270 + 30 * np.cos(t)
y = 350 - 64 * np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

plt.xlim(0, 350)
plt.savefig("Horsehead_HOMEWORK.png")

