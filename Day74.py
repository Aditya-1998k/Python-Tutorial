"""
Method Overriding--
we can override the method of 
parent class in child class
"""

class Shape:
    def __init__(self, x, y):
        self.x =x
        self.y =y

    def area(self):
        return self.x*self.y
    
rec =Shape(3,5)
print(rec.area())
"""
output
15
"""

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)

    def area(self):
        return 3.14* super().area()

circle = Circle(5)
print(circle.area())

"""
78.5
-----
Here we are overiding the base class (shape)
method area with child class (Circle) area 
methods
"""