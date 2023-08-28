"""
'is' and '==" in Python
--------------------
'is' compare exact location of object
in memory while == checks value not
location
"""

a=3
b=3
print(a is b)
print(a==b)
"""
Both will return true as 3 is contants
in python constant make one time in 
memory location as constant is immutable
so a and b both point to same memory location
True
True
"""

a = "aditya"
b = "aditya"
print(a is b)
print(a==b)

"""
Both will return true as 
a and b both point to same memory location
True
True
"""

a = (1,2)
b = (1,2)
print(a is b)
print(a==b)
"""
Both will return True as tuples
are immutable and python know it
so it will not create again in
memory
True
True
"""

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
print(a is b)
print(a==b)

"""
Since list are mutable and can change
so python will create seperate a and b
as they can change in the further process
so a and b both have differenct memory
location
a is b -- false
a == b --true as their value is equal
"""

a = None
b = None

print(a is b)
print(a==b)
print(a is None)

"""
All will return True as all 
are refering same memory
location
is -- checks identity not value
== -- checks value of variable
True
True
True
"""