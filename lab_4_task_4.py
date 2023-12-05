import numpy as np

def calc(varx):

    answer = np.zeros((1, len(varx)))
    print(varx)

    for i in range (0, len(varx)):
        y = varx[i] ** 2
        answer[0, i] = y
    
    return answer

x = np.arange(-5, 8, 1)

print(calc(x))