try:
    archivo = open('Prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo.\n')
    archivo.write('Adios.')
    archivo.write('\nprueba')
except Exception as e:
    print(e)
finally:
    archivo.close()