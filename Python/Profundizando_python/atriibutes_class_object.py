class Person:
    count_person = 0
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

person1 = Person('Juan', 'Perez')
print(person1.__dict__)
# Variable de clase
print(person1.count_person)
# Asignando un nuevo valor usando la variable
person1.count_person = 10
print(person1.__dict__)

print(Person.count_person)# Atributo de clase
print(person1.count_person)# Atributo del objeto 1

person2 = Person('Maria', 'Cifuentes')
print(person2.__dict__)
print(person2.count_person)

# Asociar un atributo de clase al vuelo
Person.count2 = 20
print(person2.count2)