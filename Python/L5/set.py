planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

#Largo
print(len(planetas))

# Revisar si un elemento esta presente
print('Marte' in planetas)

#Agregar un elemento
planetas.add('Tierra') #No acepta valores duplicados
print(planetas)

# Eliminar elementos, arroja error si no existe
planetas.remove('Tierra')
print(planetas)
# Eliminar elementos, no arroja error
planetas.discard('Jupiter')
print(planetas )

#Limpiar set
planetas.clear()
print(planetas)

#eliminar el set
#del planetas
print(planetas)