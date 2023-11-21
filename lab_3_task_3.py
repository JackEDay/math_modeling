from lab_3_task_1 import g
import numpy as np

x0 = 0
y0 = 82
v0 = 6

t = np.arange(0, 5, 0.1)
ans = np.zeros((len(t), 3))
x = x0 + v0*t
y = y0 + v0*t - (g*t**2)/2

print(ans)    

for i in range (0, len(t)):
    ans[i, 0] = t[i]
    ans[i, 1] = x[i]
    ans[i, 2] = y[i]
    
print(ans)
