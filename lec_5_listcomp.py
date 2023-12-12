symbols = 'Python'
symbol_codes = [0 * ord(symbol) for symbol in symbols]
print(symbol_codes)

symbol_code = (ord(symbol) for symbol in symbols)
print(symbol_code)