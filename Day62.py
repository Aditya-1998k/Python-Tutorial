"""
Acess Modifier in Python:
-----------------------
Access specifiers or access modifiers
in python programming are used to
limit the access of class variables and class
methods outside of class while implementing
the concepts of inheritance.
types:
    1.Public -- by default all variable in python
    2.Private
    3.Protected
"""

class Employee:
    def __init__(self):
        self.name ="Aditya"

a = Employee()
print(a.name)

"""
Aditya
--------
All the instance variable in a class
followed by self keyword  are public
accessed.
"""

"""
Private Access Modifiers:
--------------
No private keyword, but we can give weak
indicate to python by using __ (double underscore)

To access these variable
obj._className__variableName
"""

class Teachers:
    def __init__(self):
        self.__name ="Aditya"

a = Teachers()

"""
print(a.__name)
AttributeError: 'Teachers' object has no attribute '__name'
We can not access name variable directly
We need to access it like below
"""
print(a._Teachers__name)
print(a.__dir__())

"""
Aditya
Can be access indirectly
This is called Name mangling concept
----------------
['_Teachers__name', '__module__', 
'__init__', '__dict__', '__weakref__', 
'__doc__', '__new__', '__repr__', 
'__hash__', '__str__', '__getattribute__', 
'__setattr__', '__delattr__', '__lt__', 
'__le__', '__eq__', '__ne__', '__gt__', 
'__ge__', '__reduce_ex__', '__reduce__', 
'__getstate__', '__subclasshook__', 
'__init_subclass__', '__format__', 
'__sizeof__', '__dir__', '__class__']
"""

"""
Protected Access Modifiers:
Only access by a class and inside the 
class only
write variable using single underscore (_)
_varName
"""
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):
        return "Harry Bhai"
    

class Subject(Student):
    pass


obj = Student()
obj1 = Subject()

print(obj1._name)
print(obj1._funName())

"""
Harry
No mangling required (_ single underscore)
----------------
Harry Bhai
"""       

"""
It is Important to note that single
underscore(_) is just a naming 
convention, does not actually
provide any protection or restric
access to the member.
"""



