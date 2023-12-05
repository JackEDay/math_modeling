def fib(n):
    a = 0
    b = 1
    for i in range (1, n):
        print(a)
        a, b = b, a + b

n = 5
fib(15)