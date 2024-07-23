class Dog:
    no_legs = 4

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'La mascota de nombre {self.name} tiene {Dog.no_legs} patas'

lulu = Dog('Lulú')
Dino = Dog('Dino')
# cada onjeto tiene su nombre
print(lulu.name, Dino.name)
print(lulu.no_legs, Dino.no_legs, Dog.no_legs)
print(lulu)
print(Dino)
# para modificar el N° patas de los perros
Dog.no_legs = 6
print(lulu.no_legs, Dino.no_legs, Dog.no_legs)

# para solo un perro
lulu.no_legs = 4
print(lulu.no_legs, Dino.no_legs, Dog.no_legs)

print(lulu.no_legs, Dino.__class__.no_legs)

# creamos una variable desde la clase
Dog.name = 'Clase Perro'
print(lulu.name, Dino.name, Dog.name)

# Variable de clase que no esta en los objetos
Dog.no_ears = 2
print(lulu.no_ears, Dino.no_ears, Dog.no_ears)