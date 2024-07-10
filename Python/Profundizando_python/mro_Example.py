class Clase1:
    def __init__(self):
        print('Clase 1')
        
    def metodo(self):
        print('Metodo clase 1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase 2 __init__')
        super().__init__()
    def metodo(self):
        print('Metodo Clase 2')
        super().metodo()
class Clase3(Clase1):

    def __init__(self):
        print('Clase 3 __init__')
        super().__init__()
    def metodo(self):
        print('Metodo clase 3')
        super().metodo()

class Clase4(Clase2, Clase3):
    def metodo(self):
        print('Metodo clase 4')
        super().metodo()

clase4 = Clase4()
# Bases
print(Clase4.__bases__)
# mro
print(Clase4.__mro__)
# cual metodo se ejecuta
clase4.metodo()