class Contador_objetos:
    no_instancias = 0

    def __init__(self):
        self.no_instancias += 1

print('contador de instancias erroneo:')
print(Contador_objetos.no_instancias)
print(Contador_objetos().no_instancias)

# implementacion correcta
class Contador_objetos:
    no_instancias = 0

    def __init__(self):
        self.__class__.no_instancias += 1
print('contador de instancias:')
print(Contador_objetos.no_instancias)
print(Contador_objetos().no_instancias)
print(Contador_objetos().no_instancias)

