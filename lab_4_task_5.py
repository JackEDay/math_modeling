import numpy as np

def space(op, a, b, h, r):

    if op == 'Circle':
        S = np.pi * r ** 2
    
    elif op == 'Triangle':
        S = (a * h) / 2

    elif op == 'Rectangle':
        S = a * b
    
    else:
        S = "Неверный вариант."

    return S

option = "Circle"
a = 10
b = 7
h = 16
r = 5

print(space(option, a, b, h, r))
