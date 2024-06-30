# Laboratorio Rectángulo

class Rectangle:
    def __init__(self, high, weight):
        self.high = high
        self.weight = weight

    def area(self):
        return self.high * self.weight

high = int(input('Ingrese la altura de su rectangulo: '))
weight = int(input('Ingrese la base de su rectangulo: '))
calculator = Rectangle(high, weight)
print(f'El area de este rectangulo es: {calculator.area()}')

