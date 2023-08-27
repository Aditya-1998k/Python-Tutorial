"""
Enumerate Function in Python:
----------------------------
Enumerate function is a built in function
in python that allows you to loop over a sequence
(such as list, tuple or string) and get the index
and value of each elements in the sequence at the
same time.
"""

marks= [98, 55, 68 ,99, 78]

"""
Here i want if index = 3 then print("Awesome")
index=0
for mark in marks:
    print(mark)
    if index ==3:
        print("Awesome")
    index+=1

But same functionality we can get by 
enumerate function easily
"""

for index, mark in enumerate(marks):
    print(mark)
    if index ==3:
        print("awesome")

"""
output:
98
55
68
99
awesome
78
"""

for v in enumerate(marks):
    print(v)
    print(type(v))

"""
v is tuple -- first will be index and 
second will be value
------------------------------------
Output:
(0, 98)
<class 'tuple'>
(1, 55)
<class 'tuple'>
(2, 68)
<class 'tuple'>
(3, 99)
<class 'tuple'>
(4, 78)
<class 'tuple'>
"""


"""
Changing the start Index:
enumerate(list,start=1)
"""
for index, mark in enumerate(marks, start=1):
    print(mark)
    if index ==3:
        print("awesome")

"""
Output:
98
55
68
awesome
99
78
"""