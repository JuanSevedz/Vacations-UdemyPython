sumar_lambada = lambda a, b: a + b
print(sumar_lambada(2, 11))

# En una sola linea de codigo
print((lambda a,b: a + b) (2, 11))

lista_tuplas = [(1, 'b'), (2, 'f'), (5, 'a'), (4, 'c')]
lista_tuplas_ord = sorted(lista_tuplas, key=lambda tupla: tupla[0])
print(lista_tuplas_ord)
lista_tuplas_ord = sorted(lista_tuplas, key=lambda tupla: tupla[0], reverse=True)# por orden decreciente numerico
print(lista_tuplas_ord)
lista_tuplas_ord = sorted(lista_tuplas, key=lambda tupla: tupla[1])# por orden alfabético
print(lista_tuplas_ord)
lista_tuplas_ord = sorted(lista_tuplas, key=lambda tupla: tupla[1], reverse=True)# por orden decreciente alfabetico
print(lista_tuplas_ord)

# Ordenamiento, ejemplo 2:

print(list(range(-3, 4)))
# para ordenarla con el valor absoluto
for i in range(-3, 4):
    print(i, i*i)

lista_ordenada = sorted(range(-3, 4), key=lambda i: i*i)
print('-'*30)
print(f'Lista ordena en el rando de -3 a 3' )

# aplicar closure a las funciones lambda
def show(titulo):
    return lambda message: titulo + '. ' + message
showw_eng = show('Ingeniero')
show_lic = show('Licenciado')
print(showw_eng('Juan Felipe'))
print(show_lic('Miryam Jhoana'))