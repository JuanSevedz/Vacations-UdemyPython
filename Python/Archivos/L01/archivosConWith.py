#with open('Prueba.txt', 'r', encoding='utf8') as archivo:
    #print(archivo.read())
from manejoArchivos import ManejoArchivos

with ManejoArchivos('Prueba.txt') as archivo:
    print(archivo.read())