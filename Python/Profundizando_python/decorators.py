# Decorators with arguments
# A decorator is a function that receives a function and returns a function (at least)
# We use it to extend the functionality of a function
# 1. Decorator function (a)
# 2. Function to be decorated (b)
# 3. Decorated function (c)
# a(b) -> c
def decorator_function_a(function_to_decorate_b):
    def decorated_function_c(*args, **kwargs):
        print('Before from decorated_function_c')
        result = function_to_decorate_b(*args, **kwargs)
        print('After from decorated_function_c')
        return result

    return decorated_function_c


@decorator_function_a
def add(a, b):
    # print(f'Sum result: {a + b}')
    return a + b

result = add(int(input('Primer valor: ')), int(input('Segundo valor: ')) )
print(f'Sum result: {result}')
