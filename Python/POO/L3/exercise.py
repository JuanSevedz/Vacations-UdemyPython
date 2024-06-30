class Vehicle:
    def __init__(self, color:str, wheels:int):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return f'Color: {self.color}, Ruedas: {self.wheels}'

class Bycicle(Vehicle):
    def __init__(self, color, wheels, tipo):
        super().__init__(color, wheels)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()}, Tipo: {self.tipo}'

class Car(Vehicle):
    def __init__(self, color, wheels, speed):
        super().__init__(color, wheels)
        self.speed = speed

    def __str__(self):
        return f'{super().__str__()}, Velocidad: {self.speed} km/h'


car1 = Car('Azul', 4, 120)
print(car1)

bike1 = Bycicle('Red', 2, 'De ruta')
print(bike1)