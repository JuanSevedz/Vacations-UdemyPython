# Alcance de Variables

var_global = 'Variable global'

def imprimir():
    print(f'Variable global desde una funcion: {var_global}')
    var_local = 'Variable local'
    print(f'Variable local desde la funcion. {var_local}')

    def nested_func():
        print(f'Variable local dentro de otra funcion(anidada): {var_local}')
    nested_func()

imprimir()