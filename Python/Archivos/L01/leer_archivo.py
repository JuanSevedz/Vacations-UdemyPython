
archivo = open('Prueba.txt', 'r', encoding='utf8') #Hay que especificar la ruta en donde se encuentra el archivo txt
#print(archivo.read())#Linea para hacer que el programa lea el programa

#Leer algunos caracteres
#print(archivo.read(5))
#print(archivo.read(4))

#Leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

# Iterar archivo
#for linea in archivo:
 #   print(linea)

#Leer lineas
#print(archivo.readlines())

#Accerder solo a una linea de la lista
#print(archivo.readlines()[1])


"""
Funcion para leer y copiar informacion de un archivo a otro
"""
#Abrir un nuevo archivo
archivo2 = open('Copia.txt', 'w')
archivo2.write(archivo.read())

archivo.close()
archivo.close()
print('Se ha termina el proceso de leer y copiar archivos')