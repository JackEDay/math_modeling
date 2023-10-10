a = int(input('Введите колличествo:  '))
b = a + 2
x = 1
y = 1
for i in range (1, b):
    print(x)
    x, y = y, x + y
    print(y)