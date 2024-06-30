for i in range(11):
    if i % 3 == 0:
        print(i)


#2
print('Segundo ejerciocio de 2-6')
rango = range(2,7)
for i in rango:
    print(i)

#3
print('Tercero: rango de 3 a 10, con incremento de 2 en 2')

count = 3
for i in range(11):
    if count < 11:
        print(count)
        count = count + 2
print('Another way')
increment = range(3,11,2)
for i in increment:
    print(i)


#4: list and tuples
numbers = (13, 1, 8, 3, 2, 5, 8)

numbersList = list(numbers)
numbersList.remove(13)
numbersList.remove(8)
numbersList.remove(5)
numbersList.remove(8)
numbers= tuple(numbersList)
print(numbersList)

#Another solution

tupla=(13,1,8,3,2,5,8)
lista=[]
for element in tupla:
    if element < 5:
        lista.append(element)
print(lista)


