import mysql.connector # type: ignore

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sarita2023",
    database="personas_db"
)

cursor = personas_db.cursor()
sentencia_sql = ('DELETE FROM personas WHERE id = %s')
valor = (int(input('Id a eliminar datos: ')),)
cursor.execute(sentencia_sql, valor)
personas_db.commit()
print('Usuario eliminado')
cursor.close()