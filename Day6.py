#VARIABLE AND DATA TYPES

a=1

#I asking python to store 1 into my memory and 
#give the reference to a 
b='Harry'

# support i write Harry=1, so python will understand Harry as variable
# thats why we need to write string into quote

print(a, b)

# print(a+b)  
#both should be of same data types other wise it will throw error
#     print(a+b)  
#          ~^~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Checking data types of a, b
c = [1,2,3]
d = ('tiger','lion')
e = {"abandoned":"left", "lion":"king of forest"}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# output
# <class 'int'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>


"""
Types of data types in Python
    1.Number ---complex, integer, float
    2.String--- ''
    3.Boolean  (True/False)
    4.sequence data -- list(mutable)/tuple(immutable)
    5.Mapped data --dict (key value pair)
In python, everything is object that we need to take care always
"""