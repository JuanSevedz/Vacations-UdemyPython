# Bool conatains True or False
#Numeric Types-> False for 0, True for each others
value = 0
result = bool(value)
print(f'Valor: {value}, resultado: {result}')
value = 15.0
result = bool(value)
print(f'Valor: {value}, resultado: {result}')

#str type -> False for '', True for each others
value = ''
result = bool(value)
print(f'Valor: {value}, resultado: {result}')
value = 'Hola'
result = bool(value)
print(f'Valor: {value}, resultado: {result}')

#Collections type -> False for [NoVlues], True for each others
value = []
result = bool(value)
print(f'Valor: {value}, resultado: {result}')
value = [1,2,3]
result = bool(value)
print(f'Valor: {value}, resultado: {result}')

#Tuple Type
value = ()
result = bool(value)
print(f'Valor: {value}, resultado: {result}')
value = (12,312,1)
result = bool(value)
print(f'Valor: {value}, resultado: {result}')

#Dictionaries
value = {}
result = bool(value)
print(f'Valor: {value}, resultado: {result}')
value = {'name':'Juan', 'last_name': 'Perez'}
result = bool(value)
print(f'Valor: {value}, resultado: {result}')

if '':
    print('Regreso verdadero')
else:
    print('Regreso falso')