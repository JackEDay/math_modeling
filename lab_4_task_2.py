import numpy as np

ar = np.array([2, 4, 6, 8, 9])

def task2(ar):
    mult = 1

    for i in range (0, len(ar)):
        mult = mult * ar[i]

    return mult

print(task2(ar))