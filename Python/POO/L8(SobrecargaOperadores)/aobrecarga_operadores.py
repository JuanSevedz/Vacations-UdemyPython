# Operador +
a = 2
b = 1
print(a + b)

a = 'Hola '
b = 'Mundo'
print(a + b)

a = [1, 2, 3]
b = [6, 7, 8]
print(a + b)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad


persona1 = Persona('Juan',29)
persona2 = Persona('Felipe', 19)
print(persona1 + persona2)
print(persona1 - persona2)