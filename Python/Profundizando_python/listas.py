nombres =['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura Maria Gonzalo Hernesto'.split()
# Sumar listas
print(f'Sumar listas:{nombres + nombres2}')
# Extender una lista con otra lista
nombres.extend(nombres2)
print(f'Extender la lista1 con la lista2: {nombres}')

# Lista de números
numeros1 = [10, 40, 15, 4, 20, 9, 4]
print(f'Lista original: {numeros1}')
# Indice del primer elemento encontrado en la lista
print(f'Indice 4:{numeros1.index(4)}')

# Invertir el orden de los elemntos
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenar los elemntos de una lista
numeros1.sort()
print(f'Lista ordenanda de menor a mayor: {numeros1}')
numeros1.sort(reverse=True)
print(f'Lista ordenada de mayor a menor: {numeros1}')

# Obtener valor maximo y minimo de una lista
print(f'Valor Min: {min(numeros1)}')
print(f'Valor max: {max(numeros1)}')

# Copiar elementos de una lista a otra
numeros2 = numeros1.copy()
print(f'Lista copia: {numeros2}')
print(f'Misma referencia? {numeros1 is numeros2}')# Posicion en memoria
print(f'Mismo contenido? {numeros1 == numeros2}')# Contenido

# Slicing
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')# Posicion en memoria
print(f'Mismo contenido? {numeros1 == numeros2}')# Contenido

# Operaciones con listas
list_mult = 5 * [[2, 5]]
print(list_mult)
print(f'Misma referencia: {list_mult[0] is list_mult[1]}')
print(f'Mismo contenido? {list_mult[0] is list_mult[1]}')
list_mult[2].append(10)
print(list_mult)

# Matrices
matriz = [[12, 30], [1, 2, 3], [2, 4, 80, 6]]
print(f'Matriz original: {matriz}')
print(f'Renglon 0 columna 0: {matriz[0][0]}')
print(f'Renglon 2, columna 2: {matriz[2][2]}')

list_lists = [[10, 114, 87, 90, 7], [4,5,6,7], [9,10,12,12,12,11,14]]
list_lists.sort(key=len)
print(list_lists)

# Built-in
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(f'Ascendente A-Z: {nombres1}')
nombres1 = sorted(nombres1, reverse=True)
print(f'Descendente Z-A: {nombres1}')

# Ordenar por el largo
nombres1 = sorted(nombres1, key=len)
print(f'Segun el largo: {nombres1}')

# Built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1))