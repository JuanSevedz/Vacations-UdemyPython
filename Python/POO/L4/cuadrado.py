from geometricFigure import Geomtric_figure
from color import Color

class Cuadrado(Geomtric_figure, Color):
    def __init__(self, lado, color):
        Geomtric_figure.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.high * self.weight

    def __str__(self):
        return f'{Geomtric_figure.__str__(self)} {Color.__str__(self)}'
