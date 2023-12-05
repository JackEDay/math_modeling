import numpy as np

def calc(a, b, N):
    x = np.linspace(a, b, N)

    for i in range (0, len(x)):
        x[i] = x[i] ** 2

    return x

print(calc(-1, 1, 5))