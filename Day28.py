"""
String Formatting in python:
----------------------------
string formatting can be done in python using
the format method
"""

def intro(name, country):
    template = "Hey my name is {} and I am from {}"
    return template.format(name,country)

name =input("Enter Your Name: ")
coutry =input("Enter Your country Name: ")
print(intro(name, coutry))

"""
But here is a catch we can not use directly
into the string, we need to follow order
but now we have f-string

f-string in python
------------------
we can directly pass variable name into 
the string f""
"""

def introEnhanced(name,coutry):
    template = f"Hi my name is {name} and i am from {coutry}"
    return template

print(introEnhanced(name,coutry))


def da_calculator(basic_sal):
    da=basic_sal*5/100
    return f"Your DA is {da:.2f}"

print(da_calculator(999999))
