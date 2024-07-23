
from collections import namedtuple
# Extesion del tipo de datos -> tupla
# forma1
Persona1 = namedtuple('Persona1', 'nombre apellido edad')
# crear la instancia de la clase
persona1 = Persona1('Juan', 'Vega', 18)
# crea un repr automáticamente
print(persona1)

# forma2
# crear clase con atributos
Persona2 = namedtuple('Persona2', ['nombre', 'apellido', 'edad'])
persona2 = Persona2('Andres', 'Vega', 15)
print(persona2)

# Acceder a los atributos por nombre
print(f'Nombre: {persona2.nombre}')
print(f'Apellido: {persona2.apellido}')
print(f'Edad: {persona2.edad}')

# Ahora, los accedemos por el indice
print(f'Nombre: {persona2[0]}')
print(f'Apellido: {persona2[1]}')
print(f'Edad: {persona2[2]}')

# convertir los valores a una tupla
print(tuple(persona2))

# Hacer unpacking
nombre, apellido, edad = persona2
print(f'Valores de la tupla persona: {nombre}, {apellido}, {edad}')
# o con el *
print(*persona2)

class Persona3(Persona2):
    def mayusculas(self):
        return f'Nombre completo: {self.nombre.upper()} {self.apellido.upper()}'

persona3 = Persona3('Maria', 'Gimenez', 21)
print(persona3)

print(persona3.mayusculas())

# subclases con namedtuples

Persona4 = namedtuple('Persona4', Persona2._fields + ('email',))

persona4 = Persona4('Juan', 'Diaz', 18, 'sas@gmil.com')
print(persona4)

# Metodos de ayuda
print(persona4._fields)

diccionario_person4 = persona4._asdict()
print(diccionario_person4)