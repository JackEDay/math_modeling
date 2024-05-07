import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

image = plt.imread('horsead.jpg')
fig, ax = plt.subplots()

ax.imshow(image)

t = np.linspace(np.pi, 0, 100)
a = 50 + 47 * np.cos(t)
b = 290 - 10 * np.sin(t)

t = np.linspace(np.pi*7/6, np.pi/2, 100)
a1 = 138 + 47 * np.cos(t)
b1 = 275 - 30 * np.sin(t)

x = np.append(a, a1)
y = np.append(b, b1)

a = [140, 164]
b = [246, 115]

x = np.append(x, a)
y = np.append(y, b)

t = np.linspace(-np.pi/14, -(np.pi*5/6), 100)
a = 110 + 55 * np.cos(t)
b = 105 - 45 * np.sin(t)

x = np.append(x, a)
y = np.append(y, b)

a = [64, 90]
b = [126, 108]

x = np.append(x, a)
y = np.append(y, b)

t = np.linspace(-(np.pi*2/3), np.pi/6, 100)
a = 103 + 25 * np.cos(t)
b = 84 - 28 * np.sin(t)

x = np.append(x, a)
y = np.append(y, b)

a = [126, 151]
b = [69, 43]

x = np.append(x, a)
y = np.append(y, b)

a = [150, 210]
b = [43, 72]

x = np.append(x, a)
y = np.append(y, b)

t = np.linspace(np.pi*4/7, np.pi/8, 100)
a = 228 + 70 * np.cos(t)
b = 220 - 150 * np.sin(t)

x = np.append(x, a)
y = np.append(y, b)

a = [293, 270]
b = [160, 285]

x = np.append(x, a)
y = np.append(y, b)

t = np.linspace(np.pi/2, np.pi, 100)
a = 270 + 30 * np.cos(t)
b = 350 - 64 * np.sin(t)

x = np.append(x, a)
y = np.append(y, b)

a = [0, 245]
b = [350, 350]

x = np.append(x, a)
y = np.append(y, b)

a = [0, 245]
b = [350, 350]

x = np.append(x, a)
y = np.append(y, b)

a = [0, 0]
b = [350, 320]

x = np.append(x, a)
y = np.append(y, b)

a = 0
b = 350

x = np.append(x, a)
y = np.append(y, b)

a = 4
b = 290

x = np.append(x, a)
y = np.append(y, b)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.xlim(0, 350)
plt.plot(spline_curve[0], spline_curve[1], color='w')

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 100
x_pictures_limits = [0, 300]
y_pictures_limits = [350, 0]

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            plt.plot(x_point_coord, y_point_coord, 'wo', ms = 1) 

plt.savefig("Horsehead_HOMEWORK.png")