class Convertidor:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 200

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Temperatura demasiada alta: {celsius}')
        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Temperatura en  Fahrenheit muy alta: {fahrenheit}')

        return (fahrenheit-32)*5/9

if __name__ == '__main__':
    print('Qué desea hacer?')
    print('1.Pasar de C a F')
    print('2.Pasar de F a C')
    opcion = int(input('Seleccione la opcion: '))
    if opcion == 1:
        inp_celsius = int(input('Introduce la temperatura en celsius: '))
        result = Convertidor.c_f(inp_celsius)
        print(f'{inp_celsius}° C a Fahremheit es: {result}')
    elif opcion == 2:
        inp_fahrenheit = int(input('Introduce la temperatura en Fahrenheit:'))
        result = Convertidor.f_c(inp_fahrenheit)
        print(f'10° f a celsius es: {result}')
    else:
        print(f'Opcion {opcion} no disponible')


