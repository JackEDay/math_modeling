import numpy as np

def task2():
    n = int(input("Введите кол-во элементов массива:    "))
    ar = np.zeros([1, n])
    mult = 1

    for i in range (0, n):
        in_numb = int(input("Введите элемент:   "))
        ar[0, i] = in_numb
        print(ar)
    
    for j in range (0, n):
        mult = mult * ar[0, j]

    return(mult)

print(task2())