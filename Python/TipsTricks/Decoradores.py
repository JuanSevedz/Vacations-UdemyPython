def decorador_envolvente(funcion_a_decorar):
    # Recibir la funcion y regresarla
    print('Estamos dentro de la funcion decoradora')
    return funcion_a_decorar

# Ahora utilicemos este decorador
def saludar():
    return 'Saludos desde mi funcion...'

# Llamamos manualmente el decorador (no es común en Python)
funcion_retornada = decorador_envolvente(saludar())
print(funcion_retornada)

@decorador_envolvente
def saludar_funcion_a_decorar():
    return 'Saludos desde funcion a decorar...'


print(saludar_funcion_a_decorar())
print(' - '* 10)
# Uso de dcoradores
def mayusculas(funcion_decorar):
    def envolvente():
        resultado_or = funcion_decorar()
        modify_result = resultado_or.upper()
        return modify_result
    return envolvente

@mayusculas
def saludar_minusculas():
    return 'hola...'
print(saludar_minusculas())

print(' - ' * 30)
###########333
# Decoradores multiples
def  negritas(funcion):
    def funcion_envolvente():
        return '<strong>' + funcion() + '</strong>'
    return funcion_envolvente

def enfatizar(funcion):
    def funcion_envolvente():
        return '<em>' + funcion() + '</em>'

    return funcion_envolvente
@negritas
@enfatizar
# from bottom to top -> order
def saludar_html():
    return 'Hola HTML'

print(saludar_html())
print(' - ' * 30)
###########333
# Decoradores con args

def decorar_argunmentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        print('Se ejecuta el decorador')
        print('args', args)
        print('kwargs', kwargs)
        return funcion(*args, **kwargs)

    return funcion_envolvente

@decorar_argunmentos
def saludar(titulo, nombre):
    # print titulo con nombre
    print(f'{titulo}. {nombre}')

saludar('Ingeniero', 'Vega')
