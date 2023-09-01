"""
dunder methods in python:
-------------
These are the special methods that you 
can define in your class and when invoked,
they give you a powerful way to manipulate
object and behaviour.

Also known as dunder methods (double underscore)
eg: __init__ method is dunder method
"""

class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i=0
        for c in self.name:
            i = i+1
        return i

emp1=Employee("Harry")
print(emp1.name)
print(len(emp1))

"""
output:
Harry
5
------------------

__init__ methods --Init is a special
method that is invoked automatically
when instance of class is created.

__len__ methods -- len method is used
to get the length of an object. THis is
useful when you want to be able to find
the size of a data structure such as 
list or dictionary.
"""

"""
__str__ and __repr__ methods
these methods are used to convert 
an object to a string representation
str method is used when you want to
print out an object while the repr 
method is used when you want to get a 
string representation of an object that
can be used to recreate the object
"""

class Programmer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The name of Programmer is {self.name}"
    
    def __repr__(self):
        return f"Employee('{self.name})"
    
    def __call__(self):
        print("Hey I am good")
    
programmer1 = Programmer("Aditya")
print(str(programmer1))
print(repr(programmer1))
programmer1()

"""
The name of Programmer is Aditya
Employee('Aditya)
Hey I am good
-----
when you print object you will get return
of str methods

__call__ method is used to make object
callable, we can pass them as parameter
to a function
"""