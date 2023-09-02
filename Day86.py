"""
Walrus Operator:
-----
The walrus operator is a new addition
to python 3.8 and allows you to assign
a value to a variable within an expression.
This can be useful when you need to use a 
value multiple times in a loop, but don't
want to repeat the calculation.

:=  this is how walrus operator represented
"""

a =True
print(a:=False)

"""
Output: False
so here we assign False to a while expression
evaluation
"""

numbers = [1,2,3,4,5]
while(n := len(numbers))> 0:
    print(numbers.pop())

"""
Here at every iteration we are changing
value of n as numbers lenght is going
to decrease each time
5
4
3
2
1
"""

# foods = list()

# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# print(foods)

"""
What food do you like?: banana
What food do you like?: aloo
What food do you like?: quit
['banana', 'aloo']
Here we are doing this task without
walrus operator
"""

foods = list()

while (food:= input("What food do you like?: ")) !="quit":
    foods.append(food)

print(foods)

"""
What food do you like?: gobhi manchurian
What food do you like?: gobhi rice
What food do you like?: banana chips
What food do you like?: aloo chips
What food do you like?: quit 
['gobhi manchurian', 'gobhi rice', 'banana chips', 'aloo chips']
"""