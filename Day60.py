"""
getters and setters in Python:
-----------------
Getters in python are mthods that are
used to access the value of an object's
properties. They are used to reutrn the 
value of a spcecific property, and are
typically defined using the @property 
decorator.

getter --does not take any argument
we need setter to modify attribute
"""

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    # getter
    @property
    def ten_x_value(self):
        return 10*self._value

    #setter
    @ten_x_value.setter
    def ten_x_value(self, new_value):
        self._value = new_value/10

obj = MyClass(10)
print(obj.ten_x_value)
obj.ten_x_value = 67
obj.show()

"""
100
Value is 6.7
"""