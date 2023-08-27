"""
Local and Global variable in python
"""

x = 4 #global variable

def local_global():
    x=5 #local variable
    y=6 #local variable
    print(f"this x is local: {x}")

local_global()
print(f"this x is global: {x}")
# print(y)
"""
this x is local: 5
this x is global: 4
NameError: name 'y' is not defined
"""

"""
How to make a local var to global variable
----------------
Use keyword inside local block
to define that this variable is global
"""

num = 100

def hello():
    global num
    num = 200
    print(f"this num is global: {num}")

hello()
print(num)

"""
this num is global: 200
200
"""

"""
Note: Use this feature carefully as 
we don't need to change a global
variable inside function that is not
a good practice
"""