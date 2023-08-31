"""
dir()--dir function return the list of all the
attribute and methods (including dunder methods)
available for the object. It is useful tools for 
discovering what you can do with an object.
"""
x = [1,2,3,4,5]
print(dir(x))
print(x.__add__)
"""
    ['__add__', '__class__', '__class_getitem__', 
    '__contains__', '__delattr__', '__delitem__', 
    '__dir__', '__doc__', '__eq__', '__format__', 
    '__ge__', '__getattribute__', '__getitem__', 
    '__getstate__', '__gt__', '__hash__', '__iadd__', 
    '__imul__', '__init__', '__init_subclass__', 
    '__iter__', '__le__', '__len__', '__lt__', 
    '__mul__', '__ne__', '__new__', '__reduce__', 
    '__reduce_ex__', '__repr__', '__reversed__', 
    '__rmul__', '__setattr__', '__setitem__', 
    '__sizeof__', '__str__', '__subclasshook__', 
    'append', 'clear', 'copy', 'count', 'extend', 
    'index', 'insert', 'pop', 'remove', 'reverse', 
    'sort']
    ------------------
    <method-wrapper '__add__' of list object at 0x7f6a43d77c40>
"""

"""
__dict__
the __dict__ attribute returns a dictionary
representation of an object's attributes. It is a
useful tool for introspection.
"""




class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age

p = Person("John", 30)
print(p.__dict__)

"""
Output:
-----------
{'name': 'John', 'age': 30}
"""

"""
help()--the help function is used to
get help documentation for an object,
including a description of its attributes
and methods.
"""

print(help(Person))
"""
Output:
Help on class Person in module __main__:

class Person(builtins.object)
 |  Person(name, age)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
"""