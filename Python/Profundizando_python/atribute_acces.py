class MyClass:
    def __init__(self, publico, protegido, privado ):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

object = MyClass('Valor publico', 'Valor Protegido', 'Valor privado')
print(object.publico)
object.publico = 'Nuevo valor publico'
print(object.publico)

"""
print(object._protegido)
object._protegido = 'Nuvo valor protegido'

print(object._MyClass__privado)# forma de acceder a un objeto privado, pero que no se recomienda dejar en el codigo
"""