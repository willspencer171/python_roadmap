'''
A decorator is a design pattern in Python that allows a user to add new functionality to an
existing object without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate.
'''
#https://www.datacamp.com/tutorial/decorators-python

# A decorator is a function that encloses another function, it adds functionality to
# a function without modifying the structure
import functools

# The general structure of a decorator looks like this:
def decorator_function(function):
    def dec_wrapper(*args, **kwargs):
        # do something here
        pass
    return dec_wrapper

# decorator_function would get used as the decorator like this:
@decorator_function
def do_nothing():
    pass

# Let's use an example
def uppercase_decorator(fun):
    def wrapper(string):
        func = fun(string)
        make_uppercase = func.upper()
        print(make_uppercase)

    return wrapper

@uppercase_decorator
def say_hi(string):
    return string
    
say_hi("hello!")

# A general purpose decorator
def gen_purpose_dec(function):
    def wrapper_with_args(*args, **kwargs):
        print(f"Positional arguments are: {args}")
        print(f"Keyword arguments are: {kwargs}")
        function(*args, **kwargs)
    
    return wrapper_with_args

@gen_purpose_dec
def my_example(a, b, c, *args, **kwargs):
    print(a, b, c)

def dead_func():
    pass

my_example(1, 2, 3, 76436728, "hello", dead_func,  harvey="Spectre", greg="Wallace")

# There is an extra layer of scope we can add and that is to wrap the decorator as well
def decorator_that_takes_arguments(arg1, arg2, arg3):
    def decorator_with_wrapper(function):
        # This makes debugging easier as it allows us to see metadata for the wrapped function
        @functools.wraps(function)
        def wrapper(fun1, fun2, fun3):
            print(f"this wrapper can access variables from the upper decorator {arg1, arg2, arg3}")
            print(f"and arguments from the decorated function {fun1, fun2, fun3}")
            function(fun1, fun2, fun3)
        
        return wrapper
    return decorator_with_wrapper

@decorator_that_takes_arguments("Outer layer", "Nicest view", "big money boi")
def last_function_ill_make(fun1, fun2, fun3):
    print("This is the decorated function that can only see its own variables")
    print(fun1, fun2, fun3)

last_function_ill_make("simple", "unclever", "dumb")

# Without the @functools.wraps decorator, this prints "wrapper"
# With it, it prints the desired "last_function_ill_make"
print(last_function_ill_make.__name__)

'''
Python has a decorator library available at
https://wiki.python.org/moin/PythonDecoratorLibrary

Decorators are good as a bit of a middle ground between classes and methods
They are lightweight and add functionality without having to think about how to restructure
something you've already made

They keep your code DRY (don't repeat yourself yourself)
'''