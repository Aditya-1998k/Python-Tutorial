"""
Map, Filter and Reduce function
-------------
These are called Higher Order function as
they are taking function as arguments.

map()--the map function applies a functio to each
element in a sequence and return a new
sequence containing the transformed elements
    map(predicatefunction, iterable)

eg: Let make a list of number from another list
which will contains squere of all the element
of another list
"""

arr = [1,2,3,4,5,6,7]

newArr = list(map(lambda x: x*x, arr))
print(newArr)

"""
output: [1, 4, 9, 16, 25, 36, 49]
mapfunction takes first argument as expression
or function which will transform elements of 
input list, and second argument is the list
from which transformation happens
"""


"""
filter()--filter function filters a sequence
of elements based on given predicate (a function that
return boolean value) and return a new sequence
containing only the elements that meet the predicate

    filter(predicate, iterable)
--use list function to convert to list

ie:I want to filter all the even number from a list
"""

arr = [23, 45, 46, 989, 64, 2, 45, 6]

evenlist =list(filter(lambda x: x%2==0, arr))
print(evenlist)

"""
Output:
[46, 64, 2, 6]

filter(lambda x: x%2==0, arr) 
this will return object
<filter object at 0x7f4a7fb03f70>
Using list method to convert this to 
list

Function which we are passing as an
argument must return boolean
"""

"""
reduce()---
    1.from functools import reduce
    2.takes two argument and return single value
    3.The iterable argument is sequence of element
    4.The reduce function applies the function to
    the first two elements in the iterable
    and then applies the function to the result and
    the next element, and so on. The reduce function
    return the final result

    reduce(predicate, iterable)
"""
from functools import reduce
arr = [1,2,3,4,5,6,7,8,9]

sum = reduce(lambda x,y: x+y, arr)
print(sum)

"""
output-45
breakdown:
x=1, y=2 --3--this will be assign to x
x=3, y=3 --6
x=6, y=4 --10
x=10, y=5 --15
x=15, y=6 --21
x=21, y=7 --28
x=28, y=8 --36
x=36, y=9 --45

what ever retun will be 
given to x in the next 
iteration
"""