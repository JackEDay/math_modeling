import matplotlib.pyplot as plt
import numpy as np

def ellipse(max_grid, rad_x, rad_y, N):
    x = np.linspace(-1*max_grid, max_grid, N)
    y = np.linspace(-1*max_grid, max_grid, N)

    X, Y = np.meshgrid(x, y)

    fxy = X**2/rad_x**2 + Y**2/rad_y**2 - 1

    plt.contour(X, Y, fxy, levels=[0])
    plt.grid()
    plt.savefig('lab_6_task_3.png')

ellipse(10, 5, 10, 100)