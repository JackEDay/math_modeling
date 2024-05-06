import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

image = plt.imread('crab.jpg')
fig, ax = plt.subplots()

ax.imshow(image)

t = np.linspace(np.pi, np.pi/2.5, 100)
x1 = 400 + 180 * np.cos(t)
y1 = 500 - 220 * np.sin(t)
x2 = 420
y2 = 240

x = np.append(x1, x2)
y = np.append(y1, y2)

x1 = 460
y1 = 230

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(np.pi, np.pi/8, 100)
x1 = 600 + 150 * np.cos(t)
y1 = 200 - 180 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(np.pi*2/3, np.pi/20, 100)
x1 = 1000 + 180 * np.cos(t)
y1 = 300 - 230 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(np.pi/6, -np.pi/6, 100)
x1 = 1030 + 180 * np.cos(t)
y1 = 400 - 230 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(np.pi/30, -np.pi*2/3, 100)
x1 = 980 + 200 * np.cos(t)
y1 = 735 - 310 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(-np.pi/6, -np.pi*11/18, 100)
x1 = 440 + 500 * np.cos(t)
y1 = 870 - 300 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

x1 = 265
y1 = 1100

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(-np.pi/3, -np.pi*5/4, 100)
x1 = 185 + 160 * np.cos(t)
y1 = 950 - 150 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

t = np.linspace(-np.pi*7/9, -np.pi*277/180, 100)
x1 = 200 + 160 * np.cos(t)
y1 = 700 - 163 * np.sin(t)

x = np.append(x, x1)
y = np.append(y, y1)

x1 = 220
y1 = 500

x = np.append(x, x1)
y = np.append(y, y1)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], 'w')
plt.axis('equal')
plt.savefig('Crab_HOMEWORK.png')