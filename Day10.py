"""
Input function:
    In python we can take input from the user
    directly by taking input function.

    variable_name =input()
    variable_name1 = input ("enter you name")

    in variable_name1 we are using text to 
    display on the screen or console

    Note: Input function always return string
    so make sure use int() function if using for
    integer input
"""

var1= input("Enter first number: ")
var2= input("Enter second number: ")

print(var1+var2)
print(var1-var2)

"""
it will do string type cancatanation
let var1='10' and var2 = '12'
output== '1012'
So please use int() function if using
arithmatic operation on number

print(var1*var2)
TypeError: can't multiply sequence by non-int of type 'str'
print(var1-var2)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
"""

print("Sum of first num and second num: ",int(var1)+int(var2))
print("Sum of first num and second num: ",float(var1)+int(var2))
