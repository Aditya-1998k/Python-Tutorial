"""
List in python:
    1.ordered collection of data items
    2.can store multple value in single variable
    3.list is mutable ,can change after creattion
      append, pop etc.
    4.Seperated by comma
    5.Enclosed by square bracket
    6.Can store multiple data types in same list
"""

marks = [3, 5, 6, "Rajan"]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
marks.append(7)
print(marks)

"""
output
[3, 5, 6, 'Rajan']
<class 'list'>
3
6
[3, 5, 6, 'Rajan', 7]
"""

"""
List Index
colors   =    ["red", "yellow", "voilet]
index            0       1          2
negativ index   -3      -2         -1

index start from 0
last index = len(colors)-1

--------------------
jump index
list_name[start:end:jump]
"""

colors = ["red", "yellow", "green", "black"]
print(colors[-2])
print(colors[len(colors)-2])
print(colors[-1])
print(colors[0])
print(colors[len(colors)-1])

if "red" in colors:
    print("Yes it have red colors")
else:
    print("don't have red colors")

"""
Output:
green --- handle -ve index by converting to +ve
green --- refer this also have same output
black
red
black
"Yes it have red colors" --this also works in string
"""

colors = ["red", "yellow", "green", "black", "white", "voilet", "purple"]

print(colors[:-1])
print(colors[1:-1])
print(colors[1:4])
print(colors[1:5:2])
print(colors[1:])

"""
output
['red', 'yellow', 'green', 'black', 'white', 'voilet']
['yellow', 'green', 'black', 'white', 'voilet']
['yellow', 'green', 'black'] --last index excluding
['yellow', 'black'] -- start 1 and end 5 and jump index 2
['yellow', 'green', 'black', 'white', 'voilet', 'purple']
"""

"""
List Comprehension:
-------------------
List comprehension are used for creating
new list from other iterables like lists,
tuples, dictionaries, sets and even array
and strings.
"""
myList1 = [i for i in range(4)]
myList2 = [i*i for i in range(4)]
myList3 = [i for i in range(10) if i%2 ==0]
print(myList1)
print(myList2)
print(myList3)


nums = [78, 79, 56, 47, 78, 98]
even_list = [i for i in nums if i%2==0]
print(even_list)

"""
output
[0, 1, 2, 3]
[0, 1, 4, 9]
[0, 2, 4, 6, 8]
[78, 56, 78, 98]
"""
