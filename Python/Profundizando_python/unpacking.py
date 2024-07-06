
valores = 1,2,3
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)

valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

def regresa_varios_datos():
    return (1, 2, 3)

valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *valores_restantes = regresa_varios_datos()
print(valor1, valores_restantes)

# help(str.partition)
hora, _, minutos = '17:20'.partition(':')
# print(type(variable))
print(hora, minutos)


numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

def sumar(a, b, c):
    print(f'Resultado de la suma: {a + b + c}')

sumar(*numeros)


# Extrare elementos de la lista
my_list = [1, 2, 3, 4, 5, 6]
a, *b, c, d = my_list
print(a, b, c, d)

# Unir lista
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [list1, list2]
print(f'Lista de listas: {list3}')
list3 = [*list1, *list2]
print(f'Union de listas: {list3}')

# Unir dicc
dic1 = {'a' : 1, 'b' : 2, 'c' : 3}
dic2 = {'d' : 4, 'e' : 5, 'd' : 6}
dic3 ={**dic1, **dic2}
print(f'Diccionarios unidos: {dic3}')

# Construir listas
lista = [*'HolaMundo']
print(lista)
print(*lista, sep='')