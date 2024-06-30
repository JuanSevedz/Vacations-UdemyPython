def list_terminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

list_terminos(IDE='Integrated DEvelopment Enviroment', PK = 'Primary Key')

# 2
def desplegar_nombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres = ['Juan', 'Karla', 'Guillermo']
desplegar_nombres(nombres)