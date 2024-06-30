value1 = int(input('Escribe el valor: '))
max = 5
min = 0

in_range= (value1 >= min) and (value1<=max)
print(in_range)
if in_range:
    print(f'El valor {value1} esta dentro de rango')
else:
    print(f'El valor {value1} esta fuera del rango')