"""
This is an example of encapsulation
"""
class Persona:
    def __init__(self, name, last_name, age, *values, **terms):
        self._name = name
        self._last_name = last_name
        self._age = age
        self.values = values
        self.terms = terms
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def age(self):
        return  self._age

    @age.setter
    def age(self, age):
        self._age = age


    def show_details(self):
        print(f'Persona: {self._name} {self._last_name} {self._age} ')


    def __del__(self):
        print(f'Persona: {self._name} {self._last_name} ')


if __name__ == "__main__":
    persona1 = Persona('Juan', 'Vega', 65)
    persona1.name = 'Hola Mundo'
    persona1.last_name = 'This is a proof'
    persona1.age = 2
    persona1.show_details()
