import numpy as np
n = int(input())
m = int(input())
ar = np.zeros((n, m))

for i in range (0, n):
    for j in range (0, m):
        ar[i, j] = np.sin(n * (i+1) + m * (j + 1))
        
