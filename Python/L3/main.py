num = int(input('Proporciona un valor entre 1 y 3: '))
numText = ''
if num == 1:
    numText = 'Numero 1'
elif num == 2:
    numText = 'Numero 2'
elif num == 3:
    numText = 'NUmero 3'
else:
    numText = 'Valor fuera de rango'

print(f'Numero proporcionado: {num} : {numText}')