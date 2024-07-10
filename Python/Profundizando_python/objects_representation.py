# print(dir(object))
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return f'{self.__class__.__name__}(nombre: {self.nombre}, apellido: {self.apellido}'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Julian', 'Manrique')
# con rpr
print(f'Mi objeto persona1: {persona1!r}')
# con str
print(persona1)
# con format
print(f'{persona1}')