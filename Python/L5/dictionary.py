dic = {
    'IDE' : 'Integrated Development Enviroment',
    'OOP' : 'Object Oriented Programming',
    'DBMS': 'Database Manage System'
}
print(dic)
#largo
print(len(dic))

# Acceder a un elemento
print(dic['IDE'])#1
print(dic.get('OOP'))#2

#modificando elemntos
dic['IDE']= 'INTEGRATED DEVELOPMENT ENVIROMENT'
print(dic)

#recorrer los elementos
for termino in dic:
    print(termino)

for termin, valor in dic.items():
    print(termin, valor)

for termino in dic.keys():# Unicamente las llaves
    print(termino)

for valor in dic.values():# Unicamente los varoles asociados a las llaves
    print(valor)

#Comprobar existencia
print('IDE' in dic)

#Agregar elementos
dic['PK'] = 'Primary Key'
print(dic)

#Remover elementos
dic.pop('DBMS')
print(dic)

#Limpiar el diccionario
dic.clear()
print(dic)

#Eliminar el diccionario
#del dic
print(dic)
