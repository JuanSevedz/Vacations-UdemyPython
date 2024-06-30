def sumar_variables(*args):
    resultado = 0
    for elemento in args:
        resultado += elemento
    return resultado

print(sumar_variables(3, 5, 9, 4, 5, 1))

# MUltiplicacion
def multiplicar_variables(*args):
    resultado = 1
    for elemento in args:
        resultado = resultado * elemento
    return resultado

print(multiplicar_variables(3, 5, 15))


#Recursive functions
def decrement(num):
    if num >= 1:
        print(num)
        decrement(num - 1)
    elif num == 0:
        return
    elif num < 0:
        print('Valor no apto...')
decrement(-7)



# Calculadora de impuestos
def total_pay(sin_imp,imp):
    total_pay = sin_imp + sin_imp * (imp/100)
    return total_pay
sin_imp = float(input('Ingrese el valor sin impuesto: '))
imp = float(input('Ingrese el valor porcentual del impuesto: '))
pay_imp = total_pay(sin_imp,imp)
print(f'Pago con impuesto: {pay_imp}')

# Convertidor de temperaturas
def c_to_f(c):
    c_to_f = ((9/5) * c ) +32
    return  c_to_f
def f_to_c(f):
    f_to_c = (5/9) * (f - 32)
    return f_to_c
selection = int(input('Elija la opcion: 1.celcious a fahrenheit y 2.Fahremheit a celcious: '))
if selection == 1:
    c = float(input('Ingrese aqui la temperatura en celsious: '))
    convert = c_to_f(c)
    print(f'La temperatura de celcious a fahrenheit es: {convert}°')
elif selection == 2:
    f = float(input('Ingrese aqui la temperatura en fahrenheit: '))
    convert = f_to_c(f)
    print(f'La temperatura de fahrenheit a celcious es: {convert}°')