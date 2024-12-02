import os
from dotenv import load_dotenv
import mysql.connector


load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Establecer la conexión a la base de datos
personas_db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

print("Conexión exitosa a la base de datos.")

cursor = personas_db.cursor()
sentencia_sql = ('DELETE FROM personas WHERE id = %s')
valor = (int(input('Id a eliminar datos: ')),)
cursor.execute(sentencia_sql, valor)
personas_db.commit()
print('Usuario eliminado')
cursor.close()