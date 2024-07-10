# Generators
# It is a special function, it returns a sequence of values
# suspend execution of the yield function (return will not be used)
def generator():
    yield 1
    print('Execution resumes')
    yield 2
    print('Execution resumes')
    yield 3

# We consume the generator on demand
gen = generator()
# With each call we consume a value
print(next(gen))
print(next(gen))
print(next(gen))
# If we try to consume more values ​​than the generator produces
# throw a StopIteration error
# print(next(gen))

# Consuming the values from the generator with a for loop
for value in generator():
    print(f'Generated number: {value}')