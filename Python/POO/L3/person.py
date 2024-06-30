class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person: Nombre: {self.name}, Edad: {self.age}'
class Employ(Person):
    def __init__(self, sueldo, name, age):
        super().__init__(name, age)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'


if __name__ == "__main__":
    employ1 = Employ(500, 'Juan', 20)
    print(employ1.name)
    print(employ1.age)
    print(employ1.sueldo)