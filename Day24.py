"""
tuples in python:
    1.ordered collection of data items
    2.Multiple items in single variable
    3.tuples seperated by commas
    4.sorrounded by ()
    5.with single element use , atleast
    6.Immutable cannot changed after created
"""

tup =(1)
print(type(tup))
tup = ("element")
print(type(tup))

"""
<class 'int'>
<class 'str'>
To make above as tuple use comma
"""

tup1 = (1,)
tup2 = ("now it is tuple",)
print(type(tup1))
print(type(tup2))
"""
output:
<class 'tuple'>
<class 'tuple'>
"""

tup = (1,2,3,4,5,6,7)
print(tup[-1])
print(tup[2])
"""
Output:
7 --convert to positive index (lenght-(negative index))
3

what if i do: tup[0]=1
TypeError: 'tuple' object does not support item assignment
"""

tup = (1,2,3,4,5,6,7)

if 7 in tup:
    print("Yeh! 7 is available in tup")

"""
tup[1:4]--same as list
"""
