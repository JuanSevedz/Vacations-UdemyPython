#fomra para evitar definir el commit y el autocommit
import psycopg2 as bd

connection = bd.connect(user = 'postgres', password = 'Sarita2023', host = '127.0.0.1', port = '5432', database = 'test_db',)

try:
    with connection:
        with connection.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Felipe', 'Diaz', 'fdiaz@mail.com')

            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = 18'
            valores = ('Sergio', 'Jaimes', 'Jjaimes@mail.com')
            cursor.execute(sentencia, valores)

            #----------------------------------

except Exception as e:
    connection.rollback()
    print(f'Ocurrio un error: {e}, se hizo rollback de la transacción')

finally:
    connection.close()

print(f'Se hizo commit')