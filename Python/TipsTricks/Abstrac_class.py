from abc import ABCMeta,abstractmethod


class ClaseBase1:
    def metodo_1(self):
        raise NotImplementedError

    def metodo_2(self):
        raise NotImplementedError

class ClaseHija(ClaseBase1):
    def metodo_1(self):
        print('Metodo uno (1) implementado...')



clase_base1 = ClaseBase1()
clase_concreta = ClaseHija()
clase_concreta.metodo_1()

# Ahora, usando abstractclass
class Base2(metaclass=ABCMeta):
    @abstractmethod
    def metodo_1(self):
        pass

    @abstractmethod
    def metodo_2(self):
        pass
class ClaseHija2(Base2):
    def metodo_1(self):
        print(f'Metodo uno implementado...')

    def metodo_2(self):
        print('Implementando metodo 2')


clase_concreta2 = ClaseHija2()
clase_concreta2.metodo_2()