# Porfundizandoen 'sets'-> susu elemnetos deben ser inmutables
# Profundizar en set
conjunto = {'Juan', True, 18.0}
print(conjunto)
# Set vacío
# conjunto = {} genera un dict vacío
# print(type(conjunto))
# set vacío correcto
conjunto = set()
print(conjunto)
print(type(conjunto))
# Mutable
conjunto.add('Juan')
print(conjunto)
# Contiene valores únicos
conjunto.add('Juan')
print(conjunto)
# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)
# Podemos agregar más elementos o incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (copia poco profunda, solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f'Es igual en contenido? {conjunto == conjunto_copia}')
print(f'Es la misma referencia? {conjunto is conjunto_copia}')

# Operaciones entre conjuntos
black_hair = {'Juan', 'Carla', 'Pedro', 'Andres'}
ruby_hair = {'Alejandro', 'Ramon', 'Vale'}
brown_eyes = {'Carla', 'Vale'}
younger_30 = {'Juan', 'Carla', 'Andres'}
# 1.Ojos cafes y pelo rubio
print(brown_eyes.union(ruby_hair))
print(ruby_hair.union(brown_eyes))# Invertido
# 2.Interseccion
print(brown_eyes.intersection(ruby_hair))
# 3.Difference
print(black_hair.difference(brown_eyes))
# 4.Simetric Difference
print(black_hair.symmetric_difference(brown_eyes))
# a 'set' is on other -> subset
print(younger_30.issubset(black_hair))
# a 'set' is on other -> superset
print(younger_30.issuperset(black_hair))
# a 'set' is on other -> something on common?-> if no == True->else: False
print(black_hair.isdisjoint(ruby_hair))