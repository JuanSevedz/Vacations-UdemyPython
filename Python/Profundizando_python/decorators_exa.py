# Number generator from 1 to 5
def number_generator():
    for number in range(1,6):
        yield number
        print('Function execution resumes')

# We use the generator
generator = number_generator()
print(f'Generator object: {generator}')
print(type(generator))

# We consume the generator values
for value in generator:
    print(f'Number produced: {value}')

# Consume on demand
generator = number_generator()
try:
    print(f'we consume on demand: {next(generator)}')
    print(f'we consume on demand: {next(generator)}')
    print(f'we consume on demand: {next(generator)}')
    print(f'we consume on demand: {next(generator)}')
    print(f'we consume on demand: {next(generator)}')
    print(f'we consume on demand: {next(generator)}')
except StopIteration as e:
    print(f'Error consuming generator {e}')

# Another way to consume a generator
print('\nOtra forma')
generator = number_generator()
while True:
    try:
        value = next(generator)
        print(f'Print generated value: {value}')
    except StopIteration as e:
        print('The generator has finished iterating')
        break