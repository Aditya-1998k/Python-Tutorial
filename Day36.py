"""
Exception Handling in Python
------------------------------
exception handling is the process of
responding to unwanted or unexpeted
events when computer program runs

we want just becuase of unwanted or unexpected
our program does not stop

Now we will check without and with try except
"""

num1 = input("Enter the number: ")
num2 = input("ENter the 2nd Number: ")

# print(int(num1)+(num2))

print("this is very important lines of code")
print("this must be executed always")

"""
num1 ='harr'
num2 =12

print(int(num1)+(num2))
        ^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'harr'

but just because of invalid input from the user
important line does not get executed
To rescue such situation try-except comes to picture
"""

try:
    print(int(num1)+(num2))
except:
    print("Invalid Input from user")

print("this is very important lines of code")
print("this must be executed always")

"""
output:
Invalid Input from user
this is very important lines of code
this must be executed always
"""


try:
    print(int(num1)+(num2))
except ValueError:
    print("Expecting integer input")

print("this is very important lines of code")
print("this must be executed always")

"""
Expecting integer input
this is very important lines of code
this must be executed always
"""


arr = [1,2,3,4,5]

try:
    print(arr[0]+arr[6])
except IndexError:
    print("Index you given does not exist")

print("this is very important lines of code")
print("this must be executed always")

"""
Index you given does not exist
this is very important lines of code
this must be executed always
"""