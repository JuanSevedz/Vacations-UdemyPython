class Peliculas:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: [Nombre: {self._nombre}]'

if __name__ == '__main__':
    pelicula1 = Peliculas('ted 2')
    print(pelicula1)