"""
Hybrid Inheritance
---------
Combination of single inheritance
and multiple inheritance is called
Hybrid Class
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

class AnimalType(Animal):
    def __init__(self, name, type):
        self.name=name
        self.type=type

class Lebra(Dog, AnimalType):
    def __init__(self, name, species):
        super().__init__(name, species)

"""
Animal and Dog --single Inheritance
Animal and AnimalTYpe -- single Inheritance

Lebra , AnimalTYpe, Dog --Multiple Inheritance
------------------
so this is example of hybrid inheritance
"""

"""
Heirarchical Inheritance

multiple subclass -- from single Parent class

               -------->Child Class1----->cc11,cc12,cc13
Base Class ---|
               -------->Child class2----->c21, c22, c23

Tree Like structure
"""