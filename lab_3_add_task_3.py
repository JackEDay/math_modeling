import numpy as np

n = int(input())
m = int(input())
ar = np.zeros((n, m))
u = -99999999999999999999

for i in range (0, n):
    for g in range (0, m):
        a = int(input())
        ar[i, g] = a
        g += 1
    g = 0
    i += 1

for k in range (0, n):
    for j in range (0, m):
        if u <= ar[k, j]:
            u = ar[k, j]
    print(u, end="\n")

            