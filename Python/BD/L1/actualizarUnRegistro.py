#Para actualizar un registro en la base de datos
import psycopg2

connection = psycopg2.connect(user = 'postgres', password = 'Sarita2023', host = '127.0.0.1', port = '5432', database = 'test_db',)
try:
    with connection:
        with connection.cursor() as cursor:
            sentencia = 'UPDATE persona set nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
            cursor.execute(sentencia, valores)
            #connection.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    connection.close()