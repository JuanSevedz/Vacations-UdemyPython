class Padre:
    def __init__(self):
        print(f'Inicializador clase Padre')
    def metodo(self):
        print(f'Metodo padre')

class Son(Padre):
    # como no se define __init__ en esta clase, se llama directamente al del padre
    #pass
    # Cuando lo definimos:
    def __init__(self):
        print('Clase hijo')

        # Usando (super), podemos llamar el __init__ del padre, directamente
        super().__init__()

    # Se sobreescriben los metodos heredados
    def metodo(self):
        print('Metodo heredado de Padre, se sobreescribe')
        
        # llamando con super
        super().metodo()

#padre1 = Padre().metodo()
hijo1 = Son().metodo()