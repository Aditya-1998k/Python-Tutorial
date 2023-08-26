"""
Conditional Operator:
>, <, >=, <=, ==, !=

We will Do Driver eligible for
drive or not based on age and 
alcoholic
"""
age = int(input("Enter your age: "))

if age<18:
    print("You can Not Drive")

elif age>=18:
    alcohol = input("Do you drink Alcohol (Y/N): ")

    if alcohol=="Y":
        print("You can not drive")
    else:
        print("You can Drive")


"""
if-elif-else
checking Number is positive,
negative or zero
"""

num = int(input("Enter the value of Number: "))

if num>0 and num !=786:
    print("Number is Positive")
elif num == 0:
    print("Number is Zero")
elif num == 786:
    print("This is Special Number")
else:
    print("Number is Negative")


"""
Nested if statements
We can use if-else-elif statements
inside other if-else-elif statements

Checking You are a good boy or Not
"""
name = input("Tell Me you Name: ")
smoke = input ("Do you Smoke(Yes/No): ")

if smoke =='No':
    alcohol =input ("Do you drink (Yes/No): ")
    if alcohol =='No':
        print("Good Boy")
    else:
        print("Bad Boy")
else:
    print("Bad Boy")

