multi = (valor * valor for valor in range(1,5))
print(next(multi))
print(next(multi))
print(next(multi))
print(next(multi))

import math
suma = sum(valor * valor for valor in range(1,5))
print(f'sumando los valores da: {suma}')

lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

lista = ['Karla', 'Gomez', 22]
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador

generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)

cadena = ', '.join(lista)
print(f'La cadena generada a partir de la lista: {cadena}')