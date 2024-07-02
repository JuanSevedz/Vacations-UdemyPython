# Float type
a = 3.0
print(f'a: {a:.2f}')#.<#>f, numero de decimales que se quieren ver

a=float(10)
print(f'a: {a:.2f}')

# Exponential Notation
a =3e5
a = 3e-5
print(f'a2: {a:5f}')

# Cualquier calculo que involucre al menos un float, se convierte en float
a = 4.0 + 5
print(f'a3= {a} {type(a)}')