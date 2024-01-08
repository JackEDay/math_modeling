fio = 'КопыловСергейАндреевич'
fio = fio.upper()
a = [ord(i) for i in fio]
print(a)
fio = fio.lower()
b = [ord(i) for i in fio]
print(b)

print(f'sum: {sum(a) + sum(b)}')