from conexion import Conexion
from usuario import Usuario
from logger_base import log
from cursor_del_pool import  Cursor_del_pool
class UsuarioDAO:
    """
    Dao = Data Acces Object
    CRUD = Create Read Update Delete
    """
    _SELECIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with Cursor_del_pool() as cursor:
            cursor.execute(cls._SELECIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with Cursor_del_pool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with Cursor_del_pool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):

        with Cursor_del_pool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {usuario}')
            return cursor.rowcount


if __name__ == '__main__':
    # Insertar registros
    usuario1 = Usuario( username='Juansevedz', password='sara123')

    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Uusarios insertados: {usuarios_insertados}')

    # Actualizar un registro
    #persona1 = Persona(26, 'Sara', 'Vega', 'svega@mail.com')
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Eliminar un registro
    #persona2 = Persona(id_persona=30)
    #personas_eliminadas = PersonaDAO.eliminar(persona2)
    #log.debug(f'Personas eliminadas: {personas_eliminadas}')
    # Seleccionar objetos
    #usuarios = UsuarioDAO.seleccionar()
    #for usuario in usuarios:
        #log.debug(usuario)