age = int(input('Introduce tu edad: '))
"""
veintes = age >= 20 and age < 30

treintras = age >=30 and age < 40


if veintes or treintras :
    #print('Dentro de rango de los (20\'s) o (30\'s)')
    if veintes:
        print('Dentro de los 20\'s')
    elif treintras:
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango.')
else:
    print("Dentro de los 20's ni 30's" )
"""
if (20 <= age <30) or (30 <= age < 40):
    print('Dentro del rango de los (20\'s) o (30\'s)')
    if (20 <= age <30):
        print('Dentro de los 20\'s')
    elif (30 <= age < 40):
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango')
elif (age > 40) or (age < 20):
    print('Fuera de rango')
