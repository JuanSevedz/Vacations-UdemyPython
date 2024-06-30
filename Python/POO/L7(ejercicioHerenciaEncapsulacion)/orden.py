from products import Producto

class Orden:
    contador_ordenes = 0
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_ordenes = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total
    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_ordenes}, \n Productos: {productos_str}'


