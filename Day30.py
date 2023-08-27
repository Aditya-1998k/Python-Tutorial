"""
Recursion in python:
a function call itself is called
recursion
Recursion is the process of defining
something in therms of itself
"""

def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))
"""
breaking down
5*factorial(4)
5*(4*factoria(3))
5*(4*(3*factorial(2)))
5*(4*(3*(2*(factorial(1)))))

factoria(1)=1
factorial(0)=1
5*4*3*2*1*1
"""


"""
Fibbonacci Series:
f(0)=0
f(1)=1
f(2)=f(1)+f(0)
f(3)=f(2)+f(1)
f(n)=f(n-1)+f(n-1)
"""

def fibbonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibbonacci(n-1)+fibbonacci(n-2)

print(fibbonacci(5))

"""
breakdown:
fib(5)=fib(4)+fib(3)
      =(fib(3)+fib(2)) + (fib(2)+fib(1))
      =((fib(2)+1)+(fib(1)+0))) + ((1+0)+1)
      =(((1+0)+1)+(1+0))+1+1
      =1+1+1+1+1
      =5
"""















