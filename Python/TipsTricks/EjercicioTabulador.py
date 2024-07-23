from contextlib import contextmanager
# Ejercicio de Identador
class Identador():
    def __init__(self):
        self.nivel = 0

    def __enter__(self):
        self.nivel += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1

    def imprimir(self, texto):
        print(' '*self.nivel + texto)# Se agrega el tabulador

# Mismo ejercicio identador con contextlib
class Identador2():
    def __init__(self):
        self.nivel = 0

    @contextmanager
    def identador(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1

    def imprimir(self, texto):
        print(' ' * self.nivel + texto)


if __name__ == '__main__':
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

    # Creamos el objeto identador
    objeto = Identador2()
    with objeto.identador():
        objeto.imprimir('primer nivel con contexlib')
        objeto.imprimir('continua primer nivel con contexlib..')
        with objeto.identador():
            objeto.imprimir('segundo nivel con contexlib')
            objeto.imprimir('continua segundo nivel con contexlib...')
            with objeto.identador():
                objeto.imprimir('tercer nivel con contexlib')
                objeto.imprimir('continua tercer nivel con contexlib...')
        objeto.imprimir('fin primer nivel con contexlib')