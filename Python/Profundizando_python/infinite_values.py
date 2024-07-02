# Infinite values Management
import math
from decimal import Decimal

infinito_positivo = float('inf')
print(infinito_positivo)
print(f'Es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(infinito_negativo)
print(f'Es infinito negativo: {math.isinf(infinito_negativo)}')

#Otra forma de comprobar
infinito_positivo = math.inf
print(infinito_positivo)
print(f'Es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(infinito_negativo)
print(f'Es infinito: {math.isinf(infinito_negativo)}')

#Usando el modulo Decimal from decimal

infinito_positivo = Decimal('Infinity')
print(infinito_positivo)
print(f'Es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = Decimal('-Infinity')
print(infinito_negativo)
print(f'Es infinito: {math.isinf(infinito_negativo)}')