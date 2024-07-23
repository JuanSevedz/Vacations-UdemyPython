# (_) se usa para evitar conflictos con los KEYWORDS

def funcion1(nombre, class_):
    print('Probando el punto:', nombre, class_)

funcion1('juan', 'Nombre')

# (__) al inicio, Afecta la forma de acceder a los atributos
class Mayor:
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2
        self.__variable_privada = 3

    def get_variable_privada(self):
        return self.__variable_privada

    def __metodo_privado(self):
        print('Accediendo al metodo privado de la clase Padre')

class Menor(Mayor):
    def __init__(self):
        super().__init__()
        self.variable_publica = 'Sobreescribiendo... 1'
        self._variable_protegida = 'Sobreescribiendo... 2'
        self.__variable_privada = 'Sobreescribiendo... 3'

    def __metodo_privado(self):
        print('Accediendo al metodo privado de la clase Hija')

# en variable globales
_Prueba__variable_global = 10
class Prueba:
    def obtener_variable_global(self):
        return __variable_global

if __name__ == '__main__':
    mayor = Mayor()
    # print(dir(mayor))
    # accediendo así: da error -> print(f'Variable Privada: {mayor.__variable_privada}')
    print(f'Variable Privada: {mayor.variable_publica}')
    print(f'Variable Privada: {mayor._variable_protegida}')
    print(f'Variable Privada: {mayor._Mayor__variable_privada}')

    # Acceder al atributo privado por medio de otro metodo
    print(f'Accediendo a traves del get: {mayor.get_variable_privada()}')

    # Accediendo desde una clase hija:
    menor = Menor()
    print(f'Se publica la variable publica desde la clase hija: {menor.variable_publica}')
    print(f'Se publica la variable protegida desde la clase hija: {menor._variable_protegida}')
    # mismo error -> print(f'Se publica la variable privada desde la clase hija: {menor.__variable_privada}'
    print(f'Se publica la variable privada desde la clase hija: {menor._Menor__variable_privada}')

    # Metodos con (__)
    # Desde la clase padre
    mayor._Mayor__metodo_privado()
    # Desde la clase hijo
    menor._Menor__metodo_privado()
    menor._Menor__metodo_privado()

    # Variable global
    print(f'Accedemos a laa variable global: {_Prueba__variable_global}')

    # Usando NAME MANGLING
    prueba = Prueba()
    print(f'Usando name... : {prueba.obtener_variable_global()}')