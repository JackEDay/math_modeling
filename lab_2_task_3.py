a = int(input("Введите год   "))
if a % 100 != 0 and a/4 == a//4:
    print('Високосный')
else:
    print("Невисокосный")