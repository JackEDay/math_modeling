import matplotlib.pyplot as plt 
import numpy as np 

def plot_log():

    f = np.arange(0, np.pi*8, 0.1)
    r = np.e**(0.1*f)

    x = np.cos(f)*r
    y = np.sin(f)*r

    plt.plot(x, y)
    plt.grid( )
    plt.savefig('lab_6_task_4_first.png')

def plot_arch():

    f = np.arange(0, 8*np.pi, 0.1)
    r = 1.2 * f

    x = np.cos(f)*r
    y = np.sin(f)*r

    plt.plot(x, y)
    plt.savefig('lab_6_task_4_second.png')

def plot_rod():

    f = np.arange(0.01, 8*np.pi, 0.1)
    r = 0.2/np.sqrt(f)

    x = np.cos(f)*r
    y = np.sin(f)*r

    plt.plot(x, y)
    plt.savefig('lab_6_task_4_third.png')

def plot_rose():

    f = np.arange(0.01, 8*np.pi, 0.1)
    r = np.sin(5*f)

    x = np.cos(f)*r
    y = np.sin(f)*r

    plt.plot(x, y)
    plt.savefig('lab_6_task_4_forth.png')

plot_log()
#plot_arch()
#plot_rod()
#plot_rose()