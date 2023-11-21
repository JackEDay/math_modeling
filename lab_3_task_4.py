import numpy as np

n = 4
m = 4
ar = np.zeros((n, m))

for i in range (0, n):
    for j in range (0, m):
        k = np.sin(n * (i+1) + m * (j + 1))
        if k > 0:
            ar[i, j] = k
        else:
            ar[i, j] = 0
        
print(ar)