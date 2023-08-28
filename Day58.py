"""
Constructor in Python:
---------------
A constructor is a special method in
a class used to create and initilize an object
of a class

Constructor is invoked automatically invoked
when an object of a class is created.

def __init__(self):
    initialization

    1.Parameterized Constructor --Person class constructor
    2.Default Constructor --ABC class constructor
"""

class ABC:
    def __init__(self):
        print("Create a object and See me")

a = ABC()
b = ABC()

"""
as we created object from the class constructor
function invoked automatically
---------------------------------
Create a object and See me
Create a object and See me
"""

class Person:

    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

p1=Person("aditya", "Software Developer")
p2=Person("Kavita","HR")
# p3=Person("Rajan", "Kumar", "Gupta")

p1.info()
p2.info()

"""
aditya is a Software Developer
Kavita is a HR
-----------------------------------------
p3=Person("Rajan", "Kumar", "Gupta")
TypeError: Person.__init__() takes 3 positional arguments but 4 were given
The above error is because our init function is accepting 3 value and we are
giving four value 
------------
3value
-------
self-->object itself , n-->name, o-->occupation
"""

