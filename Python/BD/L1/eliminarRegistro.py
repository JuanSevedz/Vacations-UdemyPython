#Para eliminar un registro en la base de datos
import psycopg2

connection = psycopg2.connect(user = 'postgres', password = 'Sarita2023', host = '127.0.0.1', port = '5432', database = 'test_db',)
try:
    with connection:
        with connection.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            valor = (input('Que registro quieres eliminar: '),)
            cursor.execute(sentencia, valor)
            #connection.commit()
            registros_eliminados = cursor.rowcount
            if registros_eliminados:
                print(f'Registros eliminados: {registros_eliminados}')
            else:
                print(f'Registro no encontrado.')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    connection.close()