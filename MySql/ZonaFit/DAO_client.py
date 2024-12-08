from client import Cliente
from conexion import Connection

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM client'
    SELECCIONAR_ID = 'SELECT * FROM client WHERE id = %s'
    INSERTAR = 'INSERT INTO client (nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE client SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM client WHERE id=%s'
    
    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Connection.get_connection()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(id=registro[0], nombre=registro[1],
                                  apellido=registro[2], membresia=registro[3])
                clientes.append(cliente)
            return clientes
        
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        
        finally:
            if conexion is not None:
                cursor.close()
                Connection.liberar_connect(conexion)

    @classmethod
    def seleccionar_por_id(cls,id):
        conexion = None
        try:
            conexion = Connection.get_connection()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            # Mapeo clase
            cliente = Cliente(registro[0], registro[1],
                              registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Connection.liberar_connect(conexion)
    @classmethod
    def insertar(cls, cliente):
        """
        Inserta un cliente a la base de datos:
        Parámetros:
        Evita que se coloque el Id del
        """
        conexion = None
        try:
            conexion = Connection.get_connection()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)  # Usa los atributos del objeto cliente
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar el usuario: {e}')
            return 0  # Devuelve 0 si hay un error
        finally:
            if conexion is not None:
                cursor.close()
                Connection.liberar_connect(conexion)

    @classmethod
    def actualizar(cls, cliente):
        """
        Actualiza un cliente existente en la base de datos.
        Parámetros:
            cliente (Cliente): Objeto Cliente con atributos (id, nombre, apellido, membresia).
        """
        conexion = None
        try:
            conexion = Connection.get_connection()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar el cliente: {e}')
            return 0
        finally:
            if conexion is not None:
                cursor.close()
                Connection.liberar_connect(conexion)

    @classmethod
    def eliminar(cls, cliente):
        """
        Elimina un cliente de la base de datos.
        Parámetros:
            id_cliente (int): ID del cliente a eliminar.
        """
        conexion = None
        try:
            conexion = Connection.get_connection()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar el cliente: {e}')
            return 0
        finally:
            if conexion is not None:
                cursor.close()
                Connection.liberar_connect(conexion)


if __name__ == '__main__':
    while True:
        print('\nMenú de opciones con DB MySql:')
        print('(1) -> Ver los usuarios registrados')
        print('(2) -> Insertar Usuarios')
        print('(3) -> Actualizar Usuario')
        print('(4) -> Eliminar Usuario')
        print('(5) -> Salir del programa')

        try:
            menu = int(input('\nInserta la opción: '))

            if menu == 1:
                # Ver los usuarios registrados
                clientes = ClienteDAO.seleccionar()
                if clientes:
                    for cliente in clientes:
                        print(cliente)
                else:
                    print('No hay usuarios registrados.')

            elif menu == 2:
                # Insertar registro
                nombre = input('Nombre: ')
                apellido = input('Apellido: ')
                membresia = int(input('Membresía: '))
                cliente1 = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
                clientes_insertados = ClienteDAO.insertar(cliente1)
                print(f'Clientes insertados: {clientes_insertados}')

            elif menu == 3:
                # Actualizar registro
                id_cliente = int(input('ID del cliente a actualizar: '))
                nombre = input('Nuevo nombre: ')
                apellido = input('Nuevo apellido: ')
                membresia = int(input('Nueva membresía: '))
                cliente_actualizado = Cliente(id=id_cliente, nombre=nombre, apellido=apellido, membresia=membresia)
                filas_actualizadas = ClienteDAO.actualizar(cliente_actualizado)
                print(f'Clientes actualizados: {filas_actualizadas}')

            elif menu == 4:
                # Eliminar registro
                id_cliente_eliminar = int(input('ID del cliente a eliminar: '))
                filas_eliminadas = ClienteDAO.eliminar(Cliente(id=id_cliente_eliminar))
                print(f'Clientes eliminados: {filas_eliminadas}')

            elif menu == 5:
                print('Saliendo del programa... ¡Hasta pronto!')
                break  # Rompe el bucle y termina la ejecución

            else:
                print('Opción no disponible. Por favor, selecciona una opción válida.')

        except ValueError:
            print('Error: Por favor, ingresa un número válido.')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}')
