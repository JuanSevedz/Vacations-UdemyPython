def mi_funcion():
    print('saludos desde mi funcion')

mi_funcion()

#2 Argumentos en la funcion
def mi_funcion(name, last_name):
    print('saludos desde mi funcion')
    print(f'Nombre: {name}, Apellido: {last_name}')

mi_funcion('Juan','Perez')
mi_funcion('Carla', 'Lara')

#3 Return

def sum(a,b):
    return a + b

result = sum(5,3)
print(f'Resultado de la suma: {result}')
# o print(f'Resultado de suma: {sum(5,3)}')


#4 Valores por default para los Paraetros
def sum(a=0,b=0):
    return a + b

result = sum()
print(f'Resultado de la suma: {result}')

#5 Argumentos Variables

def list_names(*names):
    for name in names:
        print(name)

list_names('Juan', 'Felipe', 'Karla', 'Maria', 'Jhoana')
list_names('Laura', 'Carlos')