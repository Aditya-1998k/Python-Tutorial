"""
**Looping in Python**
----------------------------
Sometimes programmer wants to 
execute a line of statements
multiple times
    1.For Loop
    2.While Loop
"""


name ='Hello'

for i in name:
    if i=='l':
        print("l: This is special")

colors = ['red', 'Yellow','blue','voilets']

for color in colors:
    if color=='red':
        print("list contains red")

"""
Above example looping on string and list
output:
    l: This is special
    l: This is special
    list contains red
"""

"""
range()--this function in python we mostly
used with for loop
---------------------------------
range(arg1, arg2, arg3)
    arg1: initial point (by default 0)
    arg2: final point+1
    arg3: increment (by default 1)
"""

for i in range(4,6):
    print(i)

for i in range(5):
    print(i)

for i in range(1,11,2):
    print(i)

"""
range(4,6)
4
5
started from 4 and till 5
---------------------------
range(5)
it will start by default from 0
and end at 4
0
1
2
3
4
---------------------------
range(1,11,2)
it will start from 1 and end at 10
but with increment with 2
1
3
5
7
9
"""