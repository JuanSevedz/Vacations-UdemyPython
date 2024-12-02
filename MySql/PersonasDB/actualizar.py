import mysql.connector  # type: ignore

personas_db = mysql.connector.connect(
    host="localhost", user="root", password="Sarita2023", database="personas_db"
)

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