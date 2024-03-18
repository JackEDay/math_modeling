import numpy as np


a = [1, 2, 3, 4, 5]
b = [10, 9, 8, 7, 6]

def circle(xfirst, yfirst, C, D):

 ##   x = np.zeros(100)
##    y = np.zeros(100)
 ##   x[0] = xfirst
 ##   y[0] = yfirst

    for i in range(1, 4):

        a[i] = a[i-1]
        b[i] = b[i-1] + D

 ##       x[i] = (x[i-1]**2 - y[i-1]**2 + C)
  ##      y[i] = (2 * x[i-1] * y[i-1] + D)

        return a
    
print(circle(0.1, 0.1, 2, 5))