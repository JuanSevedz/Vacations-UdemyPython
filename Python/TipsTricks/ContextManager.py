from contextlib import contextmanager


with open('prueba.txt', 'w')as archivo:
    archivo.write('\nHolii')

# similar a:
archivo = open('prueba.txt', 'w')
try:
    archivo.write('\nPrueba 2')
finally:
    archivo.close()

# difierente a:
archivo = open('prueba.txt', 'w')
archivo.write('\nHola sin with ni try')
# hay que cerrarlo automáticamente
archivo.close()

# El contextManager en clases
class Manejo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.archivo = open(self.nombre, 'w')
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()

# Usando contextlib
@contextmanager
def manejador_archivos(nombre):
    try:
        archivo = open(nombre, 'w')
        yield archivo
    finally:
        archivo.close()





if __name__ == '__main__':

    # Probando la clase
    with Manejo('prueba.txt') as archivo:
        archivo.write('\nPrueba desde la clase')

    # Prueba con la libreria contextlib
    with manejador_archivos('prueba.txt') as archivo:
        archivo.write('\nprueba desde decorador')
        archivo.write('\nadios')

    # Prueba de Identador
    with Identador() as identador:
        identador.imprimir('primer nivel')
        with identador:
            identador.imprimir('segundo nivel')
            identador.imprimir('continua segundo nivel...')
            with identador:
                identador.imprimir('tercer nivel')
                identador.imprimir('continua tercer nivel...')
        identador.imprimir('fin primer nivel')