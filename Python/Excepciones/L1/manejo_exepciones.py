from NUmerosIdenticosException import NumerosIdenticosException
resultado = None

# Hay jerarquia en las excepciones, se deben colocar de menor jerarquia a mayor
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise  NumerosIdenticosException('Numeros identicos')
    resultado = int(a/b)
except ZeroDivisionError as e:
    print(f'Zero-Division - Ocurrió un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {e}, {type(e)}')
else:#se ejecuta solo cuando no hat errores
    print('No se arojo niniguna excepcion')
finally:# siempre se ejecuta, así haya error o no
    print('Ejecucuion del bloque finally')


print(f'Resultado: {resultado}')
print('Continuamos...')

