"""
String Slicing:
If we want to access the few character of
the string in that case we can use string 
slicing

eg: names = "Aditya, Ritesh"
I want to print first five character
print(name[startIndex:last_index])
print(name[0:4])
"""

name ="Harshvardhana"
print(name[0:4])
print(name[5:(len(name)-1)])

"""
len() method in python can give you 
lenght of string, list etc.
"""
print(len(name))

print(name[:5])
"""first index it will take 0 by default but excluding 5"""
print(name[5:])
"""last index it will take by default len(name)"""


"""
Negative Slicing
    In case of negative slicing
    second index but be greater that first
    H  E  L  L  O
    0  1  2  3  4
   -5 -4 -3 -2 -1
"""

print(name[-3:-1]) #o/p-->an
print(name[-4:-5]) #o/p-->nothing
print(name[:-1]) #full name printed