a = int(input('Введите первое число    '))
b = int(input('Введите второе число    '))
print(f'Частное = {a/b}')
if b == 0:
    print("На ноль делить нельзя")
elif a % b != 0:
    print(f'Остаток = {a/b - a//b}')
else:
    print('Остатка нет')
