import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

fig, ax = plt.subplots()

t0 = np.linspace(np.pi, 0, 10)
x0 = 2 * np.cos(t0)
y0 = 2 * np.sin(t0)

x1 = np.linspace(2, 4, 5)
y1 = np.zeros(len(x1))

t2 = np.linspace(np.pi, np.pi*2, 10)
x2 = 6 + 2 * np.cos(t2)
y2 = 2 * np.sin(t2)

#plt.plot(x0, y0, 'bo')
#plt.plot(x1, y1, 'bo')   
#plt.plot(x2, y2, 'bo')

x4 = np.append(x0, x1)
y4 = np.append(y0, y1)
x = np.append(x4, x2)
y = np.append(y4, y2)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], color='g')

plt.axis('equal')
plt.savefig("spline_complex.png")