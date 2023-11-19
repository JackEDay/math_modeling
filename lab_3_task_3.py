from lab_3_task_1 import g
import numpy as np

x0 = 0
y0 = 82
v0 = 6
t = 0

ans = np.zeros((6, 3))

for i in range (0, 6):
    x = x0 + v0*t
    y = y0 + v0*t - (g*t**2)/2
    ans[i, 0] = t
    ans[i, 1] = x
    ans[i, 2] = y
    t += 1

print(ans)