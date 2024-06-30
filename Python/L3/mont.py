month = int(input('Proporciona mes del año (1-12): '))
station = None

if (month == 1) or (month == 2) or (month == 12):
    station = 'Invierno'
elif (month == 3) or (month == 4) or (month == 5):
    station = 'Primavera'
elif (month == 6) or (month == 7) or (month == 8):
    station = 'Verano'
elif (month == 9) or (month == 10) or (month == 11):
    station = 'Otoño'
else:
    station = 'Valor de mes inexistente'
print(f'Para el mes {month} la estacion es: {station}')