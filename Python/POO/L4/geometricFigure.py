
from abc import ABC, abstractmethod
class Geomtric_figure(ABC):
    def __init__(self, high, weight):

        if self._validation_values(high):
            self._high = high

        else:
            self._high = 0
            print(f'Valor erroneo alto: {high}')

        if self._validation_values(weight):
            self._weight = weight

        else:
            self._weight = 0
            print(f'Valor erroneo ancho: {weight}')
    @property
    def high(self):
        return self._high

    """
    @high.setter
    def high(self, high):
        if self._validation_values(high):
            self._high = high
        else:
            print(f'Valor erroneo del alto: {high}')
    """
    @property
    def weight(self):
        return self._weight

    """
    @weight.setter
    def weight(self, weight):
        if self._validation_values(weight):
            self._weight = weight
        else:
            print(f'Valor erroneo del ancho: {weight}')
    """
    @abstractmethod
    def calcular_area(self):
        pass


    def __str__(self):
        return f'Figura geométrica de [Ancho: {self._weight}, Alto: {self._high} ].'

    def _validation_values(self, value):
        return True if 0 < value < 10 else False

