"""
Operator Overloading:
--------------
Operator loading is a feature in python
that allows developers to redefine the
behaviour of mathematical and comparison
operator for custom data types.
We can use mathematical Operator in our
own class
"""

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j +{self.k}k"
    
    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
v1 = Vector(3, 5, 7)
print(v1)
v2 = Vector(4, 5, 6)
print(v2)

print(v1+v2)
print(type(v1+v2))
"""
3i + 5j +7k
4i + 5j +6k
7i + 10j +13k
<class '__main__.Vector'>

Here we doing add (+) operator but it is
not using real math addition, instead of 
that it is using add operator defined
in our class -- this is called 
Operator overloading

__add__
__divmod__
__pow__
__sub__
__mul__
__truediv__
__floordiv__
--------
benefit of returning vector is
that on result we can again 
perform vector operation.
"""