"""
Generators in Python:
it is a special type of functions that allow you to create
an iterable sequence of values. A generator functions
returns a generator object, which can be used to generate
the values one by one as you iterate over it. It is powerful
tool for working with large and complex data sets, as they
allow you to generate the value on the fly, rather than
having to create and store the entire sequence in memory.

In python you can use yield statement in function to create
generator. yield statmement returns a value from the
generator and suspend the execution of function until
the next value is requested.
"""

def myGenerator():
    for i in range(10):
        yield i

gen = myGenerator()
print(next(gen))
print(next(gen))

print("Next will be printed")
for j in gen:
    print(j)

"""
Ouput:
0
1
Next will be printed
2
3
4
5
6
7
8
9

So it is not generating all the value
it is generating onthe fly as required
benefits--memory efficient and fast
value generated --only when requested

if we create list and use the value it 
will take time to create list and and 
also take memory space
"""
