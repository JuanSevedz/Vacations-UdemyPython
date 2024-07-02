from logger_base import log
from conexion import Conexion
class Cursor_del_pool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtener_conexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug(f'Se ejecuta metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberar_conexion(self._conexion)

if __name__ == '__main__':
    with Cursor_del_pool() as cursor:
        log.debug(f'Dentro del bloque with')
        cursor.execute('SELECT * FROM usuario ORDER BY id_usuario')
        log.debug(cursor.fetchall())