import numpy as np 
import time 

def consruction(M, N):
    T = 0

    for i in np.arange(M):
        print("Внешний цикл:", i)
        T += 1
        time.sleep(1)

        for j in np.arange(N):
            print("Внутренний цикл:", j)
            T += 1
            time.sleep(1)

    return T
    
print(consruction(2, 3))