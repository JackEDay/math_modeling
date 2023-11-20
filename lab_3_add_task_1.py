import numpy as np

ar_y = int(input("Размер массива:      "))
ar_x = int(input())

frst_ar = np.zeros((ar_y, ar_x))
sec_ar = np.zeros((ar_y, ar_x))
thrd_ar = np.zeros((ar_y, ar_x))

for i in range (0, ar_y):
    for g in range (0, ar_x):
        a = int(input())
        frst_ar[i, g] = a
        g += 1
    g = 0
    i += 1

i = 0
g = 0

for i in range (0, ar_y):
    for g in range (0, ar_x):
        a = int(input())
        sec_ar[i, g] = a
        g += 1
    g = 0
    i += 1
    
for k in range (0, ar_y):
    for t in range (0, ar_x):
        if frst_ar[k, t] >= sec_ar[k, t]:
            thrd_ar[k, t] = frst_ar[k, t]
        else:
            thrd_ar[k, t] = sec_ar[k, t]
        
        t += 1
    t = 0
    k += 1

print(thrd_ar)