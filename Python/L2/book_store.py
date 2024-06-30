name = input('INgrese el nombre del libro: ')
id = int(input('INgrese el id del libro: '))
cost = float(input('Precio del libro: '))
send = input('El envío s gratis (True/False): ')

if send == 'True':
    send = True
elif send == 'False':
    send = False
else:
    send = 'valor incorrecto, debe escribir True/False'

print(f'''
      Nombre del libro: {name}
      Id: {id}
      Precio: {cost}
      Envío gratuito?: {send}
''')
