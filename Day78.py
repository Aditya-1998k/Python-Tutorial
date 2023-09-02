"""
Single Inheritance in Python:
-------------
Single inheritance in Python is a type
of inheritance where a class inherits 
properties and behaviour from a single
parent class. This is simple and most
common inheritance.

class childClass(ParentClass):
    class body
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the Animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")

d =Dog("Dog", "DoggerMan")
d.make_sound()

a =Animal("Dog", "Dog")
a.make_sound()


"""
Bark!
Sound made by the Animal
"""

"""
Quick Quize:
implement the cat class usig Animal class
"""

class Cat(Animal):
    def __init__(self, name, species = "Cat", color = None):
        super().__init__(name, species)
        self.color = color

    def make_sound(self):
        print("Meow Meow")
    
    def details(self):
        print(f"I am {self.name} and i am {self.species} and my color is {self.color}")

c = Cat(name ="Catty", color="Black")
c.make_sound()
c.details()

"""
Meow Meow
I am Catty and i am Cat and my color is Black
"""