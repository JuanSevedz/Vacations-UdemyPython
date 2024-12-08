import os
from dotenv import load_dotenv
from mysql.connector import pooling, Error

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Connection:
    DATABASE = os.getenv('DATABASE')
    USERNAME = os.getenv('DB_USERNAME', 'root')
    PASSWORD = os.getenv('PASSWORD')
    HOST = os.getenv('HOST')
    DB_PORT = os.getenv('DB_PORT')
    POOL_SIZE = int(os.getenv('POOL_SIZE'))
    POOL_NAME = os.getenv('POOL_NAME')
    pool = None

    @classmethod
    def get_pool(cls):
        if cls.pool is None:
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
    def get_connection(cls):
        return cls.get_pool().get_connection()

    @classmethod
    def liberar_connect(cls, conexion):
        conexion.close()

if __name__ == '__main__':
    conexion1 = Connection.get_connection()
    Connection.liberar_connect(conexion1)
