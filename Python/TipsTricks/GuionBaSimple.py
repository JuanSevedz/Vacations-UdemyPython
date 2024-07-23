# El guion bajo simple por convencion se usa para indicar
# que una variable es temporal o sin importancia

for _ in range(0):
    print(f'Hola... {_}')

# Tambien lo podemos utilizar cuando trabajamos con tuplas
valores = ('Juan', 'Perez', 31)
nombre, _ , edad = valores
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'Apellido: {_}')

# Se puede usar como variable temporal de cualquier tipo
_ = list()
_.append(1)
_.append(2)
_.append(3)
_.append('Juan')
print(f'Variable temporal que apunta a una lista: {_}')