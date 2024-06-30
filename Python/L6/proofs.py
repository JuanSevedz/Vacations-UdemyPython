
def c_to_f(c):
    c_to_f = ((9/5) * c ) +32
    return  c_to_f
def f_to_c(f):
    f_to_c = (5/9) * (f - 32)
    return f_to_c
selection = int(input('Elija la opcion: 1.celcious a fahrenheit y 2.Fahremheit a celcious: '))
if selection == 1:
    c = float(input('Ingrese aqui la temperatura en celsious: '))
    convert = c_to_f(c)
    print(f'La temperatura de celcious a fahrenheit es: {int(convert)}°')
elif selection == 2:
    f = float(input('Ingrese aqui la temperatura en fahrenheit: '))
    convert = f_to_c(f)
    print(f'La temperatura de fahrenheit a celcious es: {int(convert)}°')