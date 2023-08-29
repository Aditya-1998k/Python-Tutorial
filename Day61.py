"""
Inheritance in Python:
When a class derives from another class.
the child class will inherit all the public
and protected properties and method
from the parent class

class Baseclass:
    body of baseclass

class DerivedClass(Baseclass):
    Body of derived class

"""
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLangauge(self):
        print(f"The default language is Python")

e1 = Employee("Rohan", 1344)
e2 = Programmer("Nithin", 122)

e1.showDetails()
e2.showDetails()
e2.showLangauge()

"""
The name of Employee: 1344 is Rohan
The name of Employee: 122 is Nithin
The default language is Python
"""