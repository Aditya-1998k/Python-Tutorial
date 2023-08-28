"""
Lambda Function in Python:
---------------
Lambda function is a small 
anonymous function without
name. I t is defined using the
lambda keyword and has following'
syntax
lambda arguments: expression
"""

# def double(x):
#     return x*2

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda a,b,c: a+b+c/3


print(double(5))
print(cube(2))
print(avg(1,2,3))

"""
Output:
10
8
4.0

We should use this for small
function where have single express
and return that

Note: Lambda function mostly use
when we pass function as an
argument to a function
"""

def appl(fx, value):
    return 6+fx(value)

print(appl(lambda x: x*x*x, 2))

"""
output:
14
"""