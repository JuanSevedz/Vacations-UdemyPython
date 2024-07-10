# Decoradores de clase
import inspect


def decorador_repr(cls):
    print('Se ejecuta el decorador de repr')
    print(f'Recibimos el objeto de la clase {cls.__name__}')

    # Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo
    # for nombre, atributo in atributos.items():
    #     print(nombre, atributo)

    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')


    firma_init = inspect.signature(cls.__init__)
    print(f'Firma metodo __init__. {firma_init}')

    # Recuperar parametros menos 'self'
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros __init__: {parametros_init}')

    # Revisar si existen '@propert'
    for parametro in parametros_init:
        es_property = isinstance(atributos.get(parametro), property)
        if not es_property:
            raise TypeError(f'No existe un método property para el parametro: {parametro}')
    # Crear el repr
    def metodo_repr(self):

        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        # NOmbres y propiedades de los parametros
        generadora_arg =(f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        lista_arg = list(generadora_arg)
        print(f'Lista generada: {lista_arg}')

        # Crear la cadena apartir de la lista
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del metodo rpr: {argumentos}')

        # Crear la forma de __repr__
        resultado_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado del formato del metodo repr: {resultado_repr}')

        return resultado_repr

    # Agregar el metodo repr a la clase
    setattr(cls, '__repr__', metodo_repr)

    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad


persona1 = Persona('Juan', 'Vega', 19)
print(persona1)

persona2 = Persona('Maria', 'Rodriguez', 19)
print(persona2)