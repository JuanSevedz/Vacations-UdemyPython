class My_class:
    variable_clase = 'Valor variable clase'
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_etsatico():
        print(My_class.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_etsatico()
        print(self.variable_instancia)
        print(self.variable_clase)

My_class.metodo_etsatico()
My_class.metodo_clase()

mi_objeto1 = My_class('Variable_instanciassss')
mi_objeto1.metodo_clase()
mi_objeto1.metodo_instancia()

mi_clase = My_class('Valor variable instancia'.center(50,'-'))
print(mi_clase.variable_instancia)
print(mi_clase.variable_clase)


mi_clase2 =My_class('Otro valor de variable instancia')
print(mi_clase2.variable_instancia)
print(mi_clase2.variable_clase)

# Añadir varibales de clase, se puede en cualquier parte del codigo
My_class.variable_clase2 = 'Hola niños'

print(My_class.variable_clase2)
print(mi_clase2.variable_clase2)
