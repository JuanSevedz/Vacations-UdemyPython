class Cube:
    def __init__(self, weight, high, prof):
        self.weight = weight
        self.high = high
        self.prof = prof
    def vol(self):
        return self.weight * self.high * self.prof

weight = int(input('Ingrese el ancho del cubo: '))
high = int(input('Ingrese la altura del cubo: '))
prof = int(input('Ingrese la profundidad del cubo: '))

calc = Cube(weight, high, prof)
print(f'El volumen de tu cubo es de: {calc.vol()}')