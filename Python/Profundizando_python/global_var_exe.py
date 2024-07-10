count = 0
def show_count():
    print(f'El numero que selecciono es: {count}')
def modify_count(c):
    global count
    count = c

modify_count(int(input('Ingrese el numero que desea mostrar: ')))
show_count()