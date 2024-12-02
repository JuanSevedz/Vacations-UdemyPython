import mysql.connector # type: ignore

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sarita2023",
    database="personas_db"
)

cursor = personas_db.cursor()

sentencia_sql = ('INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)')

valores = (input('Nombre: '), input('Apellido: '), int(input('Edad: ')))

cursor.execute(sentencia_sql, valores)
personas_db.commit() #Para guaradar los cambios
personas_db.close()