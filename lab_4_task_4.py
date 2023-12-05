import numpy as np

def calc(a, b, N):
    x = np.linspace(a, b, N)
    y = x ** 2

    return y

print(calc(-1, 1, 100))