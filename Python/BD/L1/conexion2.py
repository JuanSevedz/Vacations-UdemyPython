import psycopg2

connection = psycopg2.connect(user = 'postgres', password = 'Sarita2023', host = '127.0.0.1', port = '5432', database = 'test_db',)
try:
    with connection:
        with connection.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    connection.close()