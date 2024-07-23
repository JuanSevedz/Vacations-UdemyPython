# __str__ su objetivo es que la informacion sea legible para el usuario
# __repr__ su objetivo es que la informacion no sea ambigua
# se utilizar para hacer debugging (formato tipo constructor)
# La implementacion por default del metodo str llama a repr

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# Por default solo es muestra el nombre de la clase y id del objeto (direccion memoria)
audi_a3 = Auto('audi', 'A3', 'rojo')
print(f'Audi: {audi_a3}')

# ahora usando str
class Auto_str:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f'str: Marca: {self.marca}, modelo: {self.modelo}, color: {self.color}'

    def __repr__(self):
        return f'repr: Marca: {self.marca}, modelo: {self.modelo}, color: {self.color}'

corsa = Auto_str('chevrolet', 'corsa', 'gris')
# Formas de imprimir la informacion usando el str:
print(corsa)
print(corsa)
print(corsa.__str__())
print(str(corsa))
print('{}'.format(corsa))
print(f'{corsa}')

# ahora.... se usa el método repr
print([corsa])
print(f'{corsa!r}')

# Podemos escoger que metodo utilizar así:
print(str(corsa))
print(repr(corsa))
