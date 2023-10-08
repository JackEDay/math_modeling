a = int(input('Введите a    '))
b = int(input('Введите b    '))
c = int(input('Введите c    '))

D = (b**2)-(4*a*c)
d = D ** 0.5
xf = ((-b) + d) / (2*a)
xs = ((-b) - d) / (2*a)

if D < 0:
    print('Нет корней') 
    
elif d == 0:
    print(f'Корень: {xs} ')
    
else:
    print(f'X1 = {xf} \nX2 = {xs}')
