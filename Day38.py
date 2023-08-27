"""
Raising Custom Errors
-------------------
In python we can raise custom 
errors by using raise keyword
"""

def factorial(num):
    if num>10 or num<0:
        raise ValueError("Invalid Input")
    if num==1:
        return 1
    if num ==0:
        return 0
    return factorial(num-1)+factorial(num-2)


num = int(input("Enter the number between 1 and 10: "))
print(factorial(num))

"""
if input >10 or <0 then it will raise error
"""


"""
try:
    pass
except CustomError:
    pass
"""

"""
There are so many python class for exception
    1.floatingPointError
    2.MemoryError
    3.ImportError
    so may builtin python exception that we can
    use in our code
    for more details visit python documentation
"""

"""
Defining Exception for your nee
----------------------------
Here i want to raise datanotfound error
when try will not get the expected num2
-------------------------

class CustomExceptionName(Exception):
    pass
"""

class DataNotFoundError(Exception):
    pass

try:
    print(num2)
except:
    raise DataNotFoundError("num2 is not found")

"""
DataNotFoundError: num2 is not found
"""