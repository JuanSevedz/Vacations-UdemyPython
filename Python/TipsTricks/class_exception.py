def validar(nombre):
    if len(nombre) < 3:
        raise ValueError
    else:
        print('Validacion correcta.')

nombre1 = 'Juan'
excepcio1 = 'fe'
validar(nombre1)
#validar(excepcio1)

# class NombreCorto(ValueError):
#    pass

# def validar_improve(nombre):
#    if len(nombre) < 3:
#        raise NombreCorto(nombre)
#    else:
#        print('Validacion correcta..')

# nombre = 'ko'
# validar_improve(nombre)

class ClaseExcepcion(TypeError):
    pass
class NombreCorto(ClaseExcepcion):
    pass

def validar_improve(nombre):
    if len(nombre) < 3:
        raise NombreCorto(nombre)
    else:
        print('Validacion correcta..')
nombre = 'pi'
try:
    validar_improve(nombre)
except ClaseExcepcion as e:
    print(f'{type(e).__name__}')