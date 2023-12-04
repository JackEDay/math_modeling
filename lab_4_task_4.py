import numpy as np

def calc():

    x = np.arange(-5, 8, 1)
    answer = np.zeros((1, len(x)))
    print(x)

    for i in range (0, len(x)):
        y = x[i] ** 2
        answer[0, i] = y
    
    return answer

print(calc())