import numpy as np

custom_ar = np.array([2, 3, 4, 5, 6])

def task1(ar):
    avr = np.average(ar)
    return avr

print(task1(custom_ar))