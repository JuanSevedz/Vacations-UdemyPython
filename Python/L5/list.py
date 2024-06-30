# Definir una lista tipo str
names = ['Juan', 'Carla', 'Ricardo', 'Maria']
#IMprimir la lista
print(names)
# Acceder a elementods de la lista
print(names[0])

# Acceder al último elemento de manera inversa
print(names[-1])

# Imprimir un rango
print(names[0:2])  #no incluye el indice 2

#Ir del inicio de la lista al indice sin incluirlo
print(names[: 3])

#Desde el indice indicado hasta el final
print(names[1:])

# cambiar valores de la lista
names[3] = 'Ivone'
print(names)

# Iterar una lista
for name in names:
    print(name)
else:
    print('No existen más nombres en la lista')

# Preguntar largo de una lista
print(len(names))

# Agregar un elemento
names.append('Lorenzo') # append(), para insertar un elemento
print(names)

#Insertar un elemento en un indice en espcifico
names.insert(1, 'Octavio')
print(names)

# Remover un elemento
names.remove('Octavio')
print(names)

#Remover el ultimo valor agregado
names.pop()
print(names)

# Eliminar un elemento en un indice indicado
del names[0]
print(names)

# limpiar la lista
names.clear()
print(names)

#Borrar la lista por completo
del names
print(names)
