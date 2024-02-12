import matplotlib.pyplot as plt
import numpy as np

def hyb_plot(max_y, min_x, max_x, N):
    x = np.linspace(min_x, max_x, N)
    y = max_y/x
    plt.plot(x, y)
    plt.grid()
    plt.savefig('lab_6_task_2.png')

hyb_plot(100, 1, 100, 100)