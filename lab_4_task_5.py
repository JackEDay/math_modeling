import numpy as np

def space():
    option = input("Площадь какой фигуры найти? \n Окружность    Треугольник     Прямоугольник \n '1'\t\t'2'\t\t'3'\n")

    if option == '1':
        r = int(input("Длина радиуса:   "))
        S = np.pi * r ** 2
    
    elif option == '2':
        a = int(input("Длина основания:     "))
        h = int(input("Длина высоты:     "))
        S = (a * h) / 2

    elif option == '3':
        a = int(input("Длина первой стороны:     "))
        b = int(input("Длина второй стороны:     "))
        S = a * b
    
    else:
        S = "Неверный вариант."

    return S

print(space())
