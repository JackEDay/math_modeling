import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import shapely.geometry as geom 
import h5py
import random

left, right, down, up = 0, 1, 0, 1


class ParticlesGenerator:

    def __init__(self, N, x0=0, y0=0, intensity=[5, 5]):
        self.N = N
        self.x0 = x0
        self.y0 = y0
        self.intensity = intensity

        t = np.linspace(np.pi, np.pi/2.5, 100)
        x1 = -250 + 180 * np.cos(t)
        y1 = -150 - 220 * np.sin(t)
        x2 = -230
        y2 = -410

        x = np.append(x1, x2)
        y = np.append(y1, y2)

        x1 = -190
        y1 = -420

        x = np.append(x, x1)
        y = np.append(y, y1)

        t = np.linspace(np.pi, np.pi/8, 100)
        x1 = -50 + 150 * np.cos(t)
        y1 = -450 - 180 * np.sin(t)

        x = np.append(x, x1)
        y = np.append(y, y1)

        t = np.linspace(np.pi*2/3, np.pi/20, 100)
        x1 =  350 + 180 * np.cos(t)
        y1 = -350 - 230 * np.sin(t)

        x = np.append(x, x1)
        y = np.append(y, y1)

        t = np.linspace(np.pi/6, -np.pi/6, 100)
        x1 = 380 + 180 * np.cos(t)
        y1 = -250 - 230 * np.sin(t)

        x = np.append(x, x1)
        y = np.append(y, y1)

        t = np.linspace(np.pi/30, -np.pi*2/3, 100)
        x1 = 330 + 200 * np.cos(t)
        y1 = 85 - 310 * np.sin(t)

        x = np.append(x, x1)
        y = np.append(y, y1)

        t = np.linspace(-np.pi/6, -np.pi*11/18, 100)
        x1 = -210 + 500 * np.cos(t)
        y1 = 220 - 300 * np.sin(t)

        x = np.append(x, x1)
        y = np.append(y, y1)

        x1 = -385
        y1 = 450

        x = np.append(x, x1)
        y = np.append(y, y1)

        t = np.linspace(-np.pi/3, -np.pi*5/4, 100)
        x1 = -465 + 160 * np.cos(t)
        y1 = 300 - 150 * np.sin(t)

        x = np.append(x, x1)
        y = np.append(y, y1)

        t = np.linspace(-np.pi*7/9, -np.pi*277/180, 100)
        x1 = -450 + 160 * np.cos(t)
        y1 = 50 - 163 * np.sin(t)

        x = np.append(x, x1)
        y = np.append(y, y1)

        x1 = -430
        y1 = -150

        x = np.append(x, x1)/1200 + 650/1200
        y = np.append(y, y1)/1200 + 650/1200

        spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
        spline_curve = interpolate.splev(figure_spline_part, spline_coords)

        curve_coords = []
        for i in range(len(spline_curve[0])):
            curve_coords.append([spline_curve[0][i], spline_curve[1][i]])
        
        plt.plot(x, y, 'b')
        plt.savefig('crab_true.png')

        self.polygon = geom.Polygon(curve_coords)

    def density(self, x, y):  
        return np.exp(- self.intensity[0] * (x - self.x0)**2 - self.intensity[1] * (y - self.y0)**2)

    def points_generator(self):

        i = 0
        while i < self.N:
            x = np.random.uniform(left, right)
            y = np.random.uniform(down, up)

            p = geom.Point(x, y)

            z = np.random.uniform(0.0, 1.0)
            if z <= self.density(x, y) and p.within(self.polygon):
                particle_coords.append([x, y])
                i += 1


particle_coords = []
rho = ParticlesGenerator(20000, 300/1200, 650/1200, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 500/1200, 775/1200, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 0.8, 0.8, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 850/1200, 250/1200, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 1140/1200, 780/1200, [30, 30])
rho.points_generator()

rho = ParticlesGenerator(20000, 150/1200, 1100/1200, [30, 30])
rho.points_generator()

x_array = np.array(particle_coords)[:, 0]
y_array = np.array(particle_coords)[:, 1]


plt.ylim(1, 0)
plt.plot(x_array, y_array, 'bo', ms=0.2)
plt.savefig("crab_false.png")