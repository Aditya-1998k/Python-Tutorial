"""
Multilevel Inheritance in Python
-----------
This is type of inheritance where
derived class inherits from another
derived class
    --repeat code avoidable

class BaseClass:
    base class code

class DerivedClass1(BaseClass):
    derived class 1 code

class DerivedClass2(DerivedClass1):
    derived class 2 code


a--grandfater
b--fater
c--son    

a--->b--->c
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed
    
    def showDetails(self):
        Animal.showDetails(self)
        print(f"Breed: {self.breed}")

class LebraDog(Dog):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name, breed = "LebraDog")

    def showDetails(self):
        Dog.showDetails(self)
        print(f"Color: {self.color}")

d = LebraDog("Tiger", "Black")
d.showDetails()

"""
Output:
----
Name : Tiger
Species : Dog
Breed: LebraDog
Color: Black
"""

d = Dog("Tiger", "Black")
d.showDetails()
print(Dog.mro())
"""
Name : Tiger
Species : Dog
Breed: Black

[<class '__main__.Dog'>, <class '__main__.Animal'>, 
 <class 'object'>]
"""
