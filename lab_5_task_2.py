name = 'Sergey Kopylov'
name_str = "_".join(name)

print('С _ :', name_str)
print('Верхний регистр:', name_str.upper())

name_up_r = name_str.upper()
name_up_r_codes = [ord(symbol) for symbol in name_up_r]
print('ASCII:', name_up_r_codes)

name = name.lower()
name_codes = [ord(symbol) for symbol in name]
print('ASCII:', name_codes)

frstmin = min(name_up_r_codes)
scndmin = min(name_codes)
lmin = [frstmin, scndmin]

print('min:', min(lmin))

frstmax = max(name_up_r_codes)
scndmax = max(name_codes)
lmax = [frstmax, scndmax]

print('max:', max(lmax))