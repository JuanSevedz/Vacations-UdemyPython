from Employ import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(objeto.mostrar_detalles())
    print(type(objeto))
    if isinstance(objeto, Gerente):# Metodo isinstance para seguridad
        print(objeto.departamento)


empleado = Empleado('Jose', 123)
imprimir_detalles(empleado)

Gerente1 = Gerente('Juan', 1200, 'Ventas')
imprimir_detalles(Gerente1)


