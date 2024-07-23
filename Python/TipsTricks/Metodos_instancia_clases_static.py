# Diferencias entre los metodos de clase, instancia y static
class MiClase:
    def metodo_instancia(self):
        return f'Metodo de instancia ejecutado... ', self

    @classmethod
    def metodo_clase(cls):
        return 'Metodo de clase ejecutado', cls

    @staticmethod
    def metodo_static():
        return 'Metodo estatico ejecutado'

# 1. Metodos de instancia
# de manera implicita
prueba = MiClase()
print(prueba.metodo_instancia())
# de manera explicita
print(MiClase.metodo_instancia(prueba))
# desde la clase
print(MiClase.metodo_instancia(MiClase))

# 2. Metodo de clase
print(MiClase.metodo_clase())
# desde las instancias accedemos a los metodos de clase
print(prueba.metodo_clase())

# 3. Metodo static
print(MiClase.metodo_static())
# desde la instacia
print(prueba.metodo_static())