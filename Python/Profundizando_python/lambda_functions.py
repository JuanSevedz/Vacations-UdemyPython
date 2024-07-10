# Lambda functions
# They are anonymous functions, and they are small (one line of code)

# It is not possible to assign a function to a variable
# my_function = def add(a, b): return a + b

# With an anonymous, unnamed lambda( function, and a single line of code
# No need to add parentheses for parameters
# You do not need to use the return word, but you must return an expression
my_lambda_function = lambda a, b: a + b

result = my_lambda_function(6,6)
print(f'Result added with lambda function: {result}')

# Lambda function that does not receive arguments (we must return a valid expression)
my_lambda_function = lambda: 'Function without arguments'
print(f'Call lambda function without arguments: {my_lambda_function()}')

# Lambda function with default parameters
my_lambda_function = lambda a=2, b=3: a + b
print(f'Result default arguments: {my_lambda_function()}')

# Lambda function with variable arguments *args and **kwargs
my_lambda_function = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Result variable arguments: {my_lambda_function(1,2,3, a=5,b=6)}')

# Lambda functions with arguments, variable arguments and default values
my_lambda_function = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Lambda function result: {my_lambda_function(1,2,4, 5,6,7,e=5,f=7)}')