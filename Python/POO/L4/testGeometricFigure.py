from geometricFigure import Geomtric_figure
from cuadrado import Cuadrado
from  RECTANGULO import Rectangulo


# NO se puede instanciar una clase abstracta
#figura = Geomtric_figure()



print(f'Creacion objeto cuadrado'.center(50,'-'))

cuadrado1 = Cuadrado(5, 'Rojo')
print(cuadrado1)
print(f'El area del cuadrado es: {cuadrado1.calcular_area()}')
print(Cuadrado.mro())


print(f'Creacion objeto rectangulo'.center(50,'-'))

rectangulo1 = Rectangulo(2,1,'Rojo')
print(rectangulo1)
print(f'El area del rectangulo es de: {rectangulo1.calcular_area()}')