""""
TYPE CASTING:
The conversion of one data type to another
data type is called typecasting
"""

a = '100'
b = '200'

print(a+b)
# since both a and b both are string so 
# it will not give exact expected answer
# output-- 100200

"""
How to do type casting in python:
    Python provide variety of function or method
    for type casting
    1.int()
    2.float()
    3.str()
    4.ord()
    5.hex(), oct()
    6.tuple(), list(), dict()

    these method will try to convert one type to other but
    that input should be valid
"""
print(int(a)+int(b))

"""
c = '1Aditya'
print(int(c))

we will get below error
ValueError: invalid literal for int() with base 10: '1Aditya'
here we are giving invalid data for type casting
"""

"""
Type of Typecasting
    1.Implicit --automatic by python itself
    2.Explicit --when we do as per requirement
"""

num1 = 1.9
num2 = 2

print(num1+num2)
"""
Here we will get output as float
here num1 is float and num2 is integer
but result is float (implicit conversion)
"""