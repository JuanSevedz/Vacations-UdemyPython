import copy


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punto({self.x!r}, {self.y!r})'

    def __eq__(self, other):
        return isinstance(other, Punto) and self.x == other.x and self.y == other.y



puntoA = Punto(3, 2)
# Para una copia poco profuanda:..
puntoB = copy.copy(puntoA)

print(f'Copia poco profunda (shallow)')
print(f'Punto A: {puntoA}')
print(f'Punto B: {puntoB}')
print(f'Por tanto, son objetos con el mismo contenido?: R/{puntoA == puntoB}')
print(f'Son los mismos onejtos(referencia)?: R/{puntoA is puntoB}')


# Otra clase..
class Rectangulo:
    def __init__(self, sup_izq, inf_der):
        self.sup_izq = sup_izq
        self.inf_der = inf_der

    def __repr__(self):
        return f'Rectangulo({self.sup_izq!r}, {self.inf_der!r})'

recA = Rectangulo(Punto(0,1), Punto(4, 3))
# copia superficial(shallow)
rectB = copy.copy(recA)
print(f'Copia superficial de los rectangulos')
print(f'Rectangulo A: {recA}')
print(f'Rectangulo B: {rectB}')

# CAMBIOS EN PUNTOS QUE AFECTA A AMBOS RECTANGULOS
recA.inf_der.y = 6
print(f'Rectangulo A: {recA}')
print(f'Rectangulo B: {rectB}')

# CON UNA COPIA PROFUNDA
rectC = copy.deepcopy(recA)
rectC.sup_izq.x = 2# Con la copia profunda, hace que no se afecten ñlos dos rectangulos, solo al que se quiere editar
print(f'Rectangulo A: {recA}')
print(f'Rectangulo C: {rectC}')
