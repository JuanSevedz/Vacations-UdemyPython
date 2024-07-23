# Tips And Tricks
def may(text):
    return text.upper()

print(may('hola'))

# Usar una funcion como un objeto
variable_func = may
print(may)
print(variable_func)
# se asigna la referencia de la funcion, apuntan a la misma
print(variable_func('conviertiendo a mayusculas'))

# si borramos la referencia...
# del may

print(variable_func('asasas'))
# print(may('asjkjkjas')), se quita el apuntador

# Saber el nombre default de una funcion
print(f'Nombre default: {variable_func.__name__}')

# Almacenar funciones en una estructura
list_fun = [may, variable_func, str.upper]
print(list_fun)

for funcion in list_fun:
    print(funcion, funcion('provando la funcion en el ciclo'))

# Accediendo directamente
print(list_fun[1]('Provandola directamene'))
print('-')
#####################
# Podemos pasar funciones a otras funciones
# Este tipo de funciones se conocen como higher-order functions
def minusculas(texto):
    return texto.lower()
def saludar(argumento_funcion):
    # Usamos la funcion que recibimos como argumento y devolvemos la referencia
    referencia_funcion_retornada = argumento_funcion('Hola, saludos desde mi funcion')
    print(referencia_funcion_retornada)

# Llamamos la funcion saludar, pasamos la referencia de una funcion como argumento
saludar(may)
saludar(minusculas)
"""
El clasico ejemplo de higher-order functions es la funcion map
Esta funcion toma una funcion como referencia, y un iterable, llama a la funcion
en cada elemento del iterable proporcionado
"""
print(list(map(may, ['texto1', 'texto2', 'texto3'])))
print(list(map(minusculas, ['Texto1', 'Texto2', 'Texto3'])))

# Funciones Anidadas
def show_(txt):
    # Funcion interna
    def convertir_mayusculas(t):
        return t.upper()
    # Llamamos la funcion interna
    return convertir_mayusculas(txt)
# Llamamos la funcion padre
print(show_('Llamando la interna desde afuera.....'))

# Retornamos la funcion anidada para que se pueda usar externamente
def talk(volum):
    def minusculas(txt):
        return txt.lower()
    def may(txt):
        return txt.upper()

    if volum > 0.5:
        return may
    else:
        return minusculas

# Usar la funcion
print(talk(0.6)('este es mi grito...'))
print(talk(0.2)('este es mi susurro...'))

variable_min = talk(0.4)
print(variable_min('Hablo suave, nuevamente...'))

#################################3
print('-'*50)
# Closures
def talk(texto, volumen):
    # la funcion anidada no recibe parametros
    def min():
        return texto.lower()
    def may():
        return texto.upper()

    if volumen > 0.5:
        return may()
    else:
        return min()

print(talk('hablando fuerte...', 0.8))
print(talk('HABLANDO SUAVE...', 0.2))

# Otro ejemplo
def show_(title):
    def greeting(message_):
        return title + '. ' + message_
    return greeting


show_engineer = show_('Ingeniero')
show_lic = show_('Licenciado')

print(show_engineer('Juan Vega'))
print(show_lic('Jhoan Diaz'))
#################################3
print('-'*50)
# Funciones 'callable'
print(f'Se puede llamar el objeto como funcion?: {callable(show_)}')


class Show:
    def __init__(self, title):
        self.title = title

    def __call__(self, message):
        return self.title + '. ' + message

show_doctor = Show('Doctor')
print(show_doctor('Carlos Lopez'))
