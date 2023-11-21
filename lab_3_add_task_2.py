import numpy as np

ar = np.zeros((1,5))

for i in range (0, 4):
    a = input()
    ar[0, i] = a

print(ar)

last = int(input("Введите последний элемент:       "))
pos = int(input("Введите позицию последнего элемента(0, 4):        "))

if pos < 4:
    for j in range (4, pos):
        ar[0, j] = ar[0, j + 1]
    ar[0, pos] = last

else:
    ar[0, pos] = last
            
print(ar)