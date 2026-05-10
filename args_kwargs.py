# *args -  Variable Positional Arguments

def greet(*args):
    print(args)
    print(type(args))

greet('Hello', 'Hi', 'Salaam')

# **kwargs - Variable Keyword Arguments