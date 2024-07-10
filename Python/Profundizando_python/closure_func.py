def ope(a, b):
    return lambda: a + b


mi_func_closure = ope(1,2)
print(f'Resultado de la función \'closure\': {int(mi_func_closure())}')

def operation(a, b, op):
    def sumar():
        return a + b

    def restar():
        return a - b

    def multiplicar():
        return a * b

    def dividir():
        return a / b if b != 0 else 'Error: Division por cero'

    if op == '1':
        return sumar
    elif op == '2':
        return restar
    elif op == '3':
        return multiplicar
    elif op == '4':
        return dividir
    else:
        return lambda: 'Operacion no valida'

def menu():
    print("Seleccione la operación que desea realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    op = input("Ingrese el número de la operación: ")

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    mi_func_closure = operation(a, b, op)
    print(f'Resultado de la función \'closure\': {int(mi_func_closure())}')




if __name__ == "__main__":
    menu()
