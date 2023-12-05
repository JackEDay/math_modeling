import numpy as np

def task1(ar):
    avr = np.average(ar)
    return avr

custom_ar = np.array([2, 3, 4, 5, 6])
print(task1(custom_ar))