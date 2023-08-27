"""
ShortHand in If-Else
-------------------
it will affect readibillity of the 
code when logic is complex 
so use where block is very small
"""

num1=900
num2=1000

print("Num1 is greater than num2") if num1>num2 else\
print("Num2 is greater than num1")

resutl = True if num1>num2 else False
print(resutl)

"""
Output:
Num2 is greater than num1
False
"""