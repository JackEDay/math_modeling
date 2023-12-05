import numpy as np


def calc(varx):

    varx = np.arange(-5, 8, 1)
    answer = np.zeros((1, len(x)))
    print(varx)

    for i in range (0, len(x)):
        y = varx[i] ** 2
        answer[0, i] = y
    
    return answer

x = np.arange(-5, 8, 1)

print(calc(x))