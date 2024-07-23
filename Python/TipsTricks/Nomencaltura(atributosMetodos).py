from PruebaModulo import funcion_publi
from PruebaModulo import _funcion_protegida

class Myclass:
    def __init__(self):
        self.variable_publica = 10
        self._variable_protegida = 11


# Probamos la clase
if __name__ == '__main__':
    objeto1 = Myclass()
    print(objeto1.variable_publica)
    print(objeto1._variable_protegida)

    # Acceder a las funciones del import(*)
    # OjO: si accedemos a funciones usando *, no se podran usar todas las funciones
    funcion_publi()
    _funcion_protegida()