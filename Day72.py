"""
super keyword in python:
---------
super keyword is used in python
to refer to parent class. This is
usefull specially when a class
inherits from multiple parent
classs and you want to call a method
from one of the parent class
"""

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
class Programmer(Employee):
    def __init__(self,name, id, lang):
        self.name = name
        self.id = id
        self.lang = lang

rohan = Employee("Rohan",1220)
sohan = Programmer("Sohan", 1222, "Python")

print(rohan.name, rohan.id)
print(sohan.name, sohan.id, sohan.lang)

"""
Rohan 1220
Sohan 1222 Python
-------------------------
But here programmer class construction
we can write using super keyword 
which will inherit from Employee class
"""

class Programmer(Employee):
    def __init__(self,name, id, lang):
        super().__init__(name, id)
        self.lang = lang

mohan = Programmer("Mohan", 1223, "Python")
print(mohan.name, mohan.id, mohan.lang)

"""
Output:
Mohan 1223 Python
"""