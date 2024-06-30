age = int(input('Ingrese su edad: '))
ubi = None
if (0 < age < 10):
    ubi = 'La infancia es increible'
elif (10 <= age < 20):
    ubi = 'Muchos cambios y mucho estudio...'
elif (20 <= age <= 30):
    ubi = 'Amor y comienza el trabajo'
else:
    ubi = 'Etapa de edad fuera de rango'
print(ubi)