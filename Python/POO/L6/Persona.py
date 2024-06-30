class Persona:
    CONTADOR_PERSONAS = 0
    @classmethod
    def generar_siguiente_valor(cls):
        cls.CONTADOR_PERSONAS += 1
        return cls.CONTADOR_PERSONAS


    def __init__(self, nombre, edad):
        Persona.CONTADOR_PERSONAS += 1
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona {self.id_persona}, Nombre: {self.nombre},  Edad: {self.edad}'

persona1 = Persona('juan', 20)
print(persona1)

persona2 =Persona('Karla', 30)
print(persona2)

persona3 = Persona('Eduardo', 17)
print(persona3)

Persona.generar_siguiente_valor()
persona4 = Persona('Maria', 36)
print(f'Valor contador personas: {Persona.CONTADOR_PERSONAS}')

