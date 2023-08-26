"""
Function in Python:
function will enable us to 
reuse the code again and again
whenever it is required

function is a block of code
which perform specific task
whenever we will call

    1.builtin function -- range(),lower() etc.
    2.user defined function -- def function_name:
"""

def geometric_mean(a,b):
    if isGreater(a,b):
        return (a*b)/a+b
    else:
        return "First number should be greater"

def isGreater(a,b):
    if a>b:
        return True
    else:
        return False
    
print(geometric_mean(10,11))
print(geometric_mean(12,11))
print(geometric_mean(100,99))
    

def deprecated_function():
    pass

"""
since function must have function body
so if we don't have we can use pass
"""