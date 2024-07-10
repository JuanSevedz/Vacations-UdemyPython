# Funciones Anidadas
def calculator(a, b, operation='sumar'):

     def sumar(a, b):
         return a + b
     def resta(a,b):
         return a-b

     if operation == 'sumar':
         print(f'La suma da: {sumar(a, b)}')
     elif operation == 'restar':
         print(f'La resta da: {resta(a, b)}')

calculator(5, 6)
calculator(6, 5, operation='restarsp')