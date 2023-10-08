a = int(input('Введите первую сторону   '))
b = int(input('Введите вторую сторону   '))
c = int(input('Введите третью сторону   '))
typet = ''

if (a == b or a == c or b == c) and (a != b or a != c or b != c):
    typet = 'равнобедренный'
elif a == b and a == c and c == b:
    typet = 'равносторонний'
else:
    typet = 'разносторонний'

if a + b > c and a + c > b and c + b > a:
    print(f'Треугольник может существовать. Треугольник {typet}.')
else:
    print('Треугольник не может существовать')