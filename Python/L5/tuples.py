fruits = ('Naranja', 'Banano', 'Guayaba')
print(fruits)
# sabe el largo
print(len(fruits))
#Acceder al indice
print(fruits[0])
#Nvgacion inversa
print(fruits[-1])
#accedera u rango
print(fruits[0:1])
# recorrer elemntos
for fruit in fruits:
    print(fruit, end=' ')

# DE tupla a lista

fruitsList = list(fruits)
fruitsList[0] = 'Borojó'
fruits = tuple(fruitsList)
print('\n',fruits)

# Eliminar ala tupla por completo
#del fruits
print(fruits)
