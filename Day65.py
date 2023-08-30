"""
Static Method in Python:
Static methods in python are methods that belongs
to a class rather than an instance of the class.
They are defined using the @staticmethod decorator and
do not access to the instance of class (self).
THey are called on the class itself not on an instance
of the class.
It means even if we don't have object we can call the
method by directly using class_name.
"""

class Maths:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num += n
        return self.num

    @staticmethod
    def add(a,b):
        return a+b
    

a = Maths(5)
print(a.addtonum(6))
print(a.add(5,10))

"""
11
15
Here i have create instance of class
then performed both method with instance
of class
add -- static method --no need to pass self
addtonum -- need to pass self
"""

print(Maths.add(7,8))
"""
ouput:
15
add is static method can be called directly
using class itself
---------------------------------
print(Maths.addtonum(5))
     ^^^^^^^^^^^^^^^^^
TypeError: Maths.addtonum() missing 1 required positional argument: 'n'
This method we are calling without instance of class (self)
To rescue such situation where we don't want to make
instance of class we can use static method
"""

