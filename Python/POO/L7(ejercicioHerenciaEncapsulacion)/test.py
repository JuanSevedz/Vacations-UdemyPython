from products import Producto
from orden import Orden

producto1 = Producto('Camisa', 1200)

producto2 = Producto('Pantalon', 2500)
producto3 = Producto('Calcetines', 50.00)
producto4 = Producto('Gorras', 40.66)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(f'Total de la orden 1: {orden1.calcular_total()}')

orden2 = Orden(productos2)
print(orden2)
print(f'Total de la orden 2: {orden2.calcular_total()}')