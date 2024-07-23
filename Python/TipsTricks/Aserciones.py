# Tip. Las aserciones nos pueden ayudar a depurar nuestros programas de errores de los cuales no nos podemos recuperar.

# Ejemplo 1. Revisamos si la división es entre 0
def dividir(a, b):
    # Nos aseguramos que el valor de b no es cero para poder continuar
    assert b != 0, 'División entre cero'
    print(f'Resultado de la división: {a / b}')


# Ejemplo 2: Calcular promedio de calificaciones

def ingresar_notas():
    notas = []
    while True:
        entrada = input("Ingrese una nota (o escriba 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return notas


def prom(notas):
    assert len(notas) != 0, 'Lista de calificaciones sin datos'
    print(f'El promedio de calificaciones es: {sum(notas) / len(notas)}')

# Descuento a productos

def aplicar_descuento(productos, descuento):
    precio_con_descuento = int(productos['precio'] * ( 1.0 - descuento))
    print(f'Precio con descuento aplicado: {precio_con_descuento}')
    assert 0 <= precio_con_descuento <= productos['precio']
    print('Descuento Valido...')





if __name__ == '__main__':
    # Prueba Ejemplo 1. División entre cero
    # dividir(int(input('Inserte el primer valor: ')), int(input('Inserte el segundo valor: ')))

    # Prueba Ejemplo 2.
    # notas = ingresar_notas()
    # prom(notas)

    # Prueba ejemplo 3
    productos = {'nombre' : 'camisa', 'precio' : 1500 }
    aplicar_descuento(productos, 0.10 )