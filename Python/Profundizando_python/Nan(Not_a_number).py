#NaN-> Not A Number, no es sensible a may o min
#-> Tipo de dato numerico indefinido
import math
from decimal import Decimal

# With mmath module
a = float('NaN')
print(f'a: {a}')
print(f'Is NaN (NOT A NUMBER)?: {math.isnan(a)}')

#With Decimal from decimal module
a= Decimal(float('Nan'))
print(f'a: {a}')
print(f'Is NaN (NOT A NUMBER)?: {math.isnan(a)}')
