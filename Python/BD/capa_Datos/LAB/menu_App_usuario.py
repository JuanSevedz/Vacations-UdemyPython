from usuarioDAO import UsuarioDAO
from logger_base import log
from usuario import Usuario
def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Listar usuarios")
    print("2. Agregar usuarios")
    print("3. Actualizar usarios")
    print("4. Eliminar usario")
    print("5. Salir")

def procesar_opcion(opcion):
    if opcion == "1":
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(f'\n{usuario}')
        return False

    elif opcion == "2":
        new_usuario = Usuario(username=input('Username: '), password=input('Password: '))
        usuarios_insertados = UsuarioDAO.insertar(new_usuario)
        log.info(f'Usarios insertados: {usuarios_insertados}')

    elif opcion == "3":
        upd_usuario = Usuario(id_usuario=int(input('Introduce el id: ')),
                              username=input('Nuevo Username: '),
                              password=input('Nuevo password: '))
        usuario_actu = UsuarioDAO.actualizar(upd_usuario)
        log.info(f'Usuario actualizado: {usuario_actu}')

    elif opcion == "4":
        del_usuario = Usuario(id_usuario=int(input('Usuario que deseas eliminar: ')))
        usuarios_del = UsuarioDAO.eliminar(del_usuario)
        log.info(f'Usuarios eliminados: {usuarios_del}')

    elif opcion == "5":
        print("Saliendo del programa...")
        return True
    else:
        print("Opción no válida, por favor selecciona una opción del menú.")
    return False

def main():
    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("Introduce tu opción: ")
        salir = procesar_opcion(opcion)

if __name__ == "__main__":
    main()