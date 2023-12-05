def mult(a, n):
    if a >= 0 and type(n) == int:
        a = a ** n
    return a

print(mult(2, 5))