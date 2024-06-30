from get_set import Persona

print('Creación de objetos'.center(30,'-'))# para dar formato al texto y rellenar el numero de pixeles que se quiere
persona2 = Persona('Carolina', 'Gomez', 30)
persona2.show_details()

print('Eliminacion de objetos'.center(30,'-'))
del persona2
