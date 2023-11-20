import numpy as np

n = int(input())
m = int(input())
ar = np.zeros((n, m))

for i in range (0, n):
    for j in range (0, m):
        k = np.sin(n * (i+1) + m * (j + 1))
        if k > 0:
            ar[i, j] = k
        else:
            ar[i, j] = 0

for i in range (0, n):
    ar[i, 0], ar[i, 1] = ar[i, 1], ar[i, 0]
    
print(ar)