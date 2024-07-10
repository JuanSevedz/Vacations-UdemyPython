numbers = range(10)
list_pairs = []

for number in numbers:
    if number %2 == 0:
        list_pairs.append(number*number)

print(f'Lista de pares: {list_pairs}')

# Now, we use list comprehensions
list_pairs = []
list_pairs = [number*number for number in numbers if number % 2 == 0]
print(f'Lista de pares con list_comprehensions: {list_pairs}')

# Another exam.., with two conditions
pairs = [number for number in range(50) if number%2==0 if number%6==0]
print(f'Numeros pares hasta 50 dividibles por 2 y 6: {pairs}')

# Adding if/else
list_pairs = []
list_unpairs = []
for number in range(10):
    if number % 2 == 0:
        list_pairs.append(number)
    else:
        list_unpairs.append(number)
print(f'Lista de pares: {list_pairs}')
print(f'Lista de impares: {list_unpairs}')

# Now with list comprehensions
list_pairs = []
list_unpairs = []
[list_pairs.append(number) if number % 2 == 0 else list_unpairs.append(number) for number in range(10)]
print(f'Lista de pares con comprehension: {list_pairs}')
print(f'Lista de impares con comprehension: {list_unpairs}')

# List of list's
list_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11]]

simple_list = [valor
               for sublist in list_lists
               for valor in sublist]
print(f'Lista simple: {simple_list}')

# without list comprehensions
list_pairs = []
for sublist in list_lists:
    for valor in sublist:
        if valor % 2 ==0:
            list_pairs.append(valor)
print(f'Lista de numeros pares: {list_pairs}')

# with list comprehension
list_pairs = []
list_pairs = [valor for sublist in list_lists for valor in sublist if valor % 2 == 0]
print(f'Usando list comprehension: {list_pairs}')