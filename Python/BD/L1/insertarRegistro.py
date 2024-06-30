#Para insertar solo un registro a la vez en la base de datos
import psycopg2

connection = psycopg2.connect(user = 'postgres', password = 'Sarita2023', host = '127.0.0.1', port = '5432', database = 'test_db',)
try:
    with connection:
        with connection.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'Clara@email.com')
            cursor.execute(sentencia, valores)
            #connection.commit()
            registros_insertados = cursor.rowcount
            print(registros_insertados)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    connection.close()