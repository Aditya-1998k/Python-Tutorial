"""
Arguments in Python:
    1.default arguments
    2.keyword arguments
    3.variable length arguments
    4.required arguments
"""

"""
default arguments: 
    When we will not 
    provide parameters during function
    call it will take defualt arguments
    -----------------------------------------
    def func_name(arg1=default,arg2=default)
"""

def name(fname, mname="kumar", lname="Gupta"):
    print(fname, mname, lname)

name("Aditya")
name("Aditya","")
name("Aditya","","Singh")
name("Gupta","","Aditya")

"""
output:
Aditya kumar Gupta
Aditya  Gupta
Aditya  Singh
Gupta  Aditya --take care of order
"""

"""
Keyword Arguments:
if we are using keyword arguments
then we don't need to worry 
about the order of arguments
otherwise we need to take care of
orders

if we give keyword argument to first then
it required for all
if if for 3rd it reqired for all after 3rd
but till third we need to maintain order 
"""

# name("Gupta",mname="",fname="Aditya")
name("Aditya",lname="Gupta",mname="")

"""
commmented code will throw error
TypeError: name() got multiple values for argument 'fname'
reason: without keyword the first argument goes for fname
and we also give fname keyword argument

output for 2nd:
Aditya  Gupta
"""

"""
required arguments:
we need to pass all the argument if 
used in the function otherwise it will
throw error (best solution pass defualt arg)
"""

def avg_num(a,b,c):
    print(a+b+c/3)

"""
avg_num(1,2)
TypeError: avg_num() missing 1 required positional argument: 'c'
so if we are not passing default value then make sure pass
all the value
"""
avg_num(1,2,3) #output =4


"""
variable length arguments:
sometimes we need to pass more arguments
than those defined in the actual function
This can be done using variable length
arguments
"""

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum = sum + i
    print("Average of Numbers: ", sum/len(numbers))


average(10,12,13)
average(10,12)
average(12,1,2,3,4,5,5,6,7,8)
"""
*args:tuples()
Whatever arguments we are passing that
becomes tuples that we can use in our
function
output: 
<class 'tuple'>
Average of Numbers:  11.666666666666666
<class 'tuple'>
Average of Numbers:  11.0
<class 'tuple'>
Average of Numbers:  5.3
"""

"""
If we want to pass argument as dict
**args -- dict
"""

def name(**names):
    print(type(names))
    print("Hello", names['fname'],
          names['lname'], 
          names['mname'])

name(mname="Kumar", lname="Gupta",fname="Aditya")

"""
output: 
<class 'dict'>
Hello Aditya Gupta Kumar
"""