nota = float(input('Introduce tu nota (0-10): '))
mensaje = None
if 9 <= nota <= 10:
    mensaje = 'A'
elif 8 <= nota < 9:
    mensaje = 'B'
elif 7 <= nota < 8:
    mensaje = 'C'
elif 6 <= nota < 7:
    mensaje = 'D'
elif 0 <= nota < 6:
    mensaje = 'F'
else:
    mensaje = 'Valor para nota incorrecto'

print(mensaje)