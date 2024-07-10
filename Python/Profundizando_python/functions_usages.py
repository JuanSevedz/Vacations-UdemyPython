def sum(a, b):
    return a + b
# 1.Asignar funciones a variables
my_func = sum

result = my_func(1, 2)
print(f'El resultado es: {result}')

# function like Arg
def operation(a, b, sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a, b)}')

operation(4, 5, sum)

# 3. Return a function from other one
def return_func():
    return  sum
mi_func =return_func()
print(f'resultado de la funcion retornada: {mi_func(8, 5)}')