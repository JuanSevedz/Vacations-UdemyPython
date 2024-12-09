import os
from dotenv import load_dotenv
from mysql.connector import pooling
from mysql.connector import Error

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Conexion:
    DATABASE = os.getenv('DATABASE')
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    DB_PORT = os.getenv('DB_PORT')
    HOST = os.getenv('HOST')
    POOL_SIZE = int(os.getenv('POOL_SIZE', 5))  # Valor por defecto: 5
    POOL_NAME = os.getenv('POOL_NAME', 'default_pool')
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrió un error al obtener el pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')
