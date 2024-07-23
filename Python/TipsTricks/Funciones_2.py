def imprimir(x, y, z):
    print(f'<{x}, {y}, {z}>')

imprimir(10, 3, 12)

tupla_vector = (8, 12, 3)
imprimir(*tupla_vector)

lista_vector = [4, 2, 1]
imprimir(*lista_vector)

expresion_gen = (x*x for x in range(3))
imprimir(*expresion_gen)

# En los diccionarios podemos obtener las llaves usando * o **
diccionario_vectors = {'x' : 10, 'y' : 3, 'z' : 12 }
imprimir(**diccionario_vectors)