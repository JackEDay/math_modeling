def fib(n):
    a = 0
    b = 1
    for i in range (1, n):
        print(a)
        c = a + b
        a = b
        b = c

n = 15
fib(n)