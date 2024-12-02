import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

personas_db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

print("Conexión exitosa a la base de datos.")


cursor = personas_db.cursor()
sentencia_sql = (
    "UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s"
)
valores = (
    input("Nombre: "),
    input("Apellido: "),
    int(input("Edad: ")),
    int(input("id: ")),
)

cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se cambia la información')
cursor.close()