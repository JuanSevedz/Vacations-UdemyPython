class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    @classmethod
    def crear_persona(cls):
        return cls(None, None)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

    @classmethod
    def persona_valores(cls, nombre, apellido):
        return cls(nombre, apellido)
persona1 = Persona('Juan', 'Perez')
print(persona1)

persona = Persona.crear_persona()
print(persona)

persona_con_valores = Persona.persona_valores('Karla', 'Huertas')
print(persona_con_valores)