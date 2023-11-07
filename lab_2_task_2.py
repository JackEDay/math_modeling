b = int(input('Введите первый член:  '))
q = int(input('Введите знаменатель:  '))
n = int(input('Введите кол-во членов:   '))
for i in range (1, n) :
    s = b*(q**(i-1))
    print(s)