"""
How Imports works in python
---------------------------
importing in python is the process
of loading code from a python module
into the current script.

import pandas
now pandas code loaded in my script
that i can use

use import keyword to import in the
function

    1.import math
    2.from math import sqrt
    3.from math import *
    4.from math import sqrt as squereroot
    5.import math as mt
"""
# import math
# print(math.sqrt(16))
# with math we can use all the function


# from math import sqrt, pi
# result = sqrt(16)*pi
# print(result)
# Here we are import sqrt and pi only
# so we can use them directly

# from math import *
# resutl =sqrt(16)*pi
# print(resutl)
# this is not recommended to import all the
# function if not required

# from math import sqrt as squerroot
# print(squerroot(16))
# here we can use as keyword for our
# convieniece

import math
print(dir(math))

"""
I can see all the function of math using dir
----------------------------------------------
['__doc__', '__loader__', '__name__', '__package__', 
'__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 
'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 
'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 
'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 
'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 
'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 
'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 
'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 
'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 
'tanh', 'tau', 'trunc', 'ulp']
"""

from Day30 import fibbonacci

print(fibbonacci(5))

"""
120 --day30 calling --later we will deal with this issue
5  --day30 calling --later we will deal with this issue
5  --this file calling
"""

"""
Whenever i am running this program a __pycache__ file
is being created why?
---------------------------------------------------\

The creation of __pycache__ directories is a normal 
behavior in Python and is related to the process of 
storing bytecode files. Here's what's happening in 
your code and why the __pycache__ directory is being created:

Importing the math Module:
When you run import math, Python imports the 
math module from the standard library. 
During this process, Python creates a bytecode 
version of the module and stores it in the 
__pycache__ directory. This is done to improve 
the import performance in subsequent runs.

"""