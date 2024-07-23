lista1 = [[2, 3], [4, 5], [6, 7]]
lista2 = list(lista1)
# las listas son objetos distintos
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
lista1.append([7,8])

print('Modificando la lista 1 con otros objetos')
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')

# si añadimos onjetos de la siguiente manera:
lista1[0][1] = 'A'
print('Con copia superficial')
print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')

# Hace que las listas cambien indirectamente


# Hacer copias profundas
import copy# Para hacer copias profundas (shallow)

lista3 = [[8, 7], [6, 5], [4, 3]]
lista4 = copy.deepcopy(lista3)
# comprobar que son iguales
lista3.append([2,1])
print('Distintos obejtos a nivel superior')
print(f'Lista 3: {lista3}')
print(f'Lista 4: {lista4}')

# Las sublistas son nuevos objetos
lista3[0][1] = 'A'
print(f'Lista 3: {lista3}')
print(f'Lista 4: {lista4}')

# No se afectan las dos listas, pues apuntan a diferentes referencias, en definitiva son distintas




