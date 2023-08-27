"""
Dictionary Methods
we have several built in methods
in dictionaries

update()--update dict2 to dict1
          dict1.update(dict2)
clear()--clear all the items of 
         dictionaries
pop()--we can del key-value using key
popitem()--remove last key-value pair of dict
del --delete dictionaries
del(key) --it will delete perticular key-value only

"""

emp1 = {111:"a++", 112:"b+", 117:"c++"}
emp2 ={115:"a++", 116:"b++"}

emp1.update(emp2)
print(emp1)

emp2.clear()
print(emp2)

emp1.pop(111)
print(emp1)

emp1.popitem()
print(emp1)

del emp1[112]
print(emp1)

del emp2
print(emp2)

"""
{111: 'a++', 112: 'b+', 117: 'c++', 115: 'a++', 116: 'b++'} --updated with emp2
{}  --emp2 cleared
{112: 'b+', 117: 'c++', 115: 'a++', 116: 'b++'} --pop (111)
{112: 'b+', 117: 'c++', 115: 'a++'} --popitem (116)
{117: 'c++', 115: 'a++'} -- del (112)

print(emp2)-- NameError: name 'emp2' is not defined. Did you mean: 'emp1'?
as this is already deleted before print

explore python documenation for more details on dictionaries
"""