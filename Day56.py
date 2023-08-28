"""
Introduction to Object Oriented
Programming:
-----------
Till now we have two approaches of
programming
    1.Procedurel programming
    2.Object Oriented Programming
"""

"""
Railway form --class (blueprint)
harry -->harry ki info wala form --object (entity)
tom -->tom ki info wala form --object (entity)
shubham -->shubham ki info wala form --object(entity)

want to change the name of shubham
shubham.changeName("Shubhi)

Encapsulation --internal state of object is hidden and can
only be accessed or modified through objects method. THis helps
to protect data.

Inheritance -- We can create special railway 
form with railway form

class -- class is a blueprint or a template for 
creating objects, providing initial value for the
state(member variable or attribute) and implementation
of behaviour (member function or methods).
The user defined object are created using the class
keyword
"""

class Person:
    name ="Harry"
    ocuupation = "Software Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.ocuupation}")


a = Person()
print(a.name)
print(a.ocuupation)
a.name = "Shubham"
a.ocuupation = "Accountant"
print(a.name)
print(a.ocuupation)
a.info()

"""
---------------
Initialized in class

Harry
Software Developer
-------------------
Changed attribute for object a

Shubham
Accountant
Shubham is a Accountant --methods call
"""

"""
self -- self parameter is a reference to
the current instance of the class and is
used to access variables that belongs to
the class
"""

b = Person()
b.name="Kavita"
b.ocuupation = "HR"
b.info()

"""
output:
Kavita is a HR

Conclusion: We can creat infinite number of
object using same template or class.
here we have created a and b object 
using same class or template. We are using 
the same method for both a and b
this is beauty of classes.
"""