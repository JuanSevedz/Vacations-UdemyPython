import psycopg2

connection = psycopg2.connect(
    user = 'postgres',
    password = 'Sarita2023',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db',
)
cursor = connection.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
connection.close()