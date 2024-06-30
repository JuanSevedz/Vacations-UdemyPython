class Person:
    def __init__(self):
        self.name = 'Juan'
        self.last_name = 'Vega'
        self.age = 28

person1 = Person()
print(person1.name)
print(person1.last_name)
print(person1.age)

# with args

class Persona:
    def __init__(self, name, last_name, age, *values, **terms):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.values = values
        self.terms = terms

    def show_details(self):
        print(f'Persona: {self.name} {self.last_name} {self.age} {self.values} {self.__dict__}')




persona1 = Persona('Juan', 'Vega', 65)
Persona.show_details(persona1) # First way

persona2 = Persona('Karla', 'Jimenes', 28, 2, 3, 4 ,5,  m= 'manzana', p = 'Pera')
persona2.show_details() # Second way


#Par editar valores de los obejtos
#persona1.name = 'Juan Carlos'
#persona1.last_name = 'Diaz'
#print(f'Objeto Persona1: {persona1.name} {persona1.last_name} {persona1.age}')