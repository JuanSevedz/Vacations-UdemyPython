from client import Cliente
from DAO_client import ClienteDAO


def menu():
    while True:
        print('*******Gym Vedz Fundation*******\n')
        print('(1) -> Ver los usuarios registrados')
        print('(2) -> Insertar Usuarios')
        print('(3) -> Actualizar Usuario')
        print('(4) -> Eliminar Usuario')
        print('(5) -> Salir del programa')

        try:
            opcion = int(input('\nInserta la opción: '))

            if opcion == 1:
                clientes = ClienteDAO.seleccionar()
                if clientes:
                    for cliente in clientes:
                        print(cliente)
                else:
                    print('No hay usuarios registrados.')

            elif opcion == 2:
                nombre = input('Nombre: ')
                apellido = input('Apellido: ')
                membresia = int(input('Membresía: '))
                cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
                insertados = ClienteDAO.insertar(cliente)
                print(f'Clientes insertados: {insertados}\n')

            elif opcion == 3:
                id_cliente = int(input('ID del cliente a actualizar: '))
                nombre = input('Nuevo nombre: ')
                apellido = input('Nuevo apellido: ')
                membresia = int(input('Nueva membresía: '))
                cliente = Cliente(id=id_cliente, nombre=nombre, apellido=apellido, membresia=membresia)
                actualizados = ClienteDAO.actualizar(cliente)
                print(f'Clientes actualizados: {actualizados}\n')

            elif opcion == 4:
                id_cliente = int(input('ID del cliente a eliminar: '))
                cliente = Cliente(id=id_cliente)
                eliminados = ClienteDAO.eliminar(cliente)
                print(f'Clientes eliminados: {eliminados}\n')

            elif opcion == 5:
                print('Saliendo del programa... ¡Hasta pronto!')
                break

            else:
                print('Opción no válida. Intenta nuevamente.')

        except ValueError:
            print('Error: Por favor, ingresa un número válido.')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}\n')


if __name__ == '__main__':
    menu()
