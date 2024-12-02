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


mi_cursor = personas_db.cursor()
mi_cursor.execute('SELECT * FROM personas')
resultado = mi_cursor.fetchall()
for persona in resultado:
    print(persona)
    
personas_db.close()