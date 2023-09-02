"""
Multiple Inheritance:
------------
Multiple inheritance is powerfull feature
in python that allows a class to inherits
attributes and methods from multiple 
parent classes. This can be useful in the 
situation where a class needs to inherits
functionality from multiple sources.

class ChildClass(Parent1, Parent2, Parent3):
    class Body

Here childclass is inheriting from parent1,
parent2 and parent3
"""
class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
    
    def show(self):
        print(f"My name is {self.name} and i am a {self.designation}")

class Dancer:
    def __init__(self, danceStyle):
        self.danceStyle=danceStyle

    def show(self):
        print(f"The dance is {self.danceStyle}")


class DancerEmployee(Employee, Dancer):
    def __init__(self, name, designation, danceStyle):
        self.name=name
        self.designation=designation
        self.danceStyle=danceStyle

o= DancerEmployee(name ="Sivani",designation= "HR", danceStyle="Kathalk")
print(o.show())
print(DancerEmployee.mro())

"""
My name is Sivani and i am a HR
--------------
[<class '__main__.DancerEmployee'>, 
<class '__main__.Employee'>, 
<class '__main__.Dancer'>, 
<class 'object'>]

-------------
method resolution order (mro)
-------------
class DancerEmployee(Dance, Employee)
first it will check in Dancer Class if order 
change
"""