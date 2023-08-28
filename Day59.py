"""
Decorators in Python:
Python decorators is a powerful
and versatile tool that allows 
you to modify the behaviour of functions
and methods.
They are a way to extend the functionality
of a function or method without modifying
its source code.

decorator takes another function as argument
and return new function that modifies the 
behavour of the origin function
"""

# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         fx()
#         print("Thank you for using decorator")
#     return mfx

# @greet
# def hello():
#     print("Hello World")

# @greet
# def sum():
#     print(10+12)

# @greet
# def intro():
#     print("I am Python Program")


# hello()
# sum()
# intro()

"""
to understand output visit mfx function
in decorator
-----------
Good Morning --first message
Hello World --function call
Thank you for using decorator --second message
------------
Good Morning
22
Thank you for using decorator
------------------
Good Morning
I am Python Program
Thank you for using decorator
"""

"""
Decorator with arguments:
pass *args--tuple and **kwargs--dict
to use decorator with function 
which is taking arguments
"""

def greetArgs(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thank you for using decorator")
    return mfx

@greetArgs
def sum(a,b):
    print(a+b)

sum(12,15)

"""
Good Morning
27
Thank you for using decorator
-------------------------
If we will not pass *args and **kwargs
then it will throw error that our 
function will not take arguments. Error like below you can get
----------------------
TypeError: greetArgs.<locals>.mfx() takes 0 positional arguments but 2 were given
"""

"""
Logging of a function using decorator
This is real world example
"""
import logging
logging.basicConfig(level=logging.INFO)

def logFunctionCall(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@logFunctionCall
def sum(a,b):
    return a+b

@logFunctionCall
def intro(name, id):
    return f"My name is {name} and my id is {id}"

print(sum(10,12))
print(intro("Aditya",1347))

"""
INFO:root:Calling sum with args = (10, 12), kwargs = {}
INFO:root:sum returned 22
22
------------------------------------------------------
INFO:root:Calling intro with args = ('Aditya', 1347), kwargs = {}
INFO:root:intro returned My name is Aditya and my id is 1347
My name is Aditya and my id is 1347
"""