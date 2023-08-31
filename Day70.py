"""
class Method as Alternative
Constructor:
------
"""

class Employee:
    def __init__(self, name, salary):
        self.name =name
        self.salary = salary

e = Employee("Harry", 1000)
print(f"My name is {e.name} and my salary is {e.salary}")

details = "Harry-1200"
e2= Employee(details.split("-")[0], details.split("-")[1])
print(e2.name, e2.salary)

"""
My name is Harry and my salary is 1000
Harry 1200
-----------------
Instead of doing this seperatly we can create a classmethod
for dealing with these type of datatypes so that our code
will look clean, below example where instaed of doing 
for instance directly created a class method and used with
class while creating the instance
"""


class EmployeeWithMethod:
    def __init__(self, name, salary):
        self.name =name
        self.salary = salary

    @classmethod
    def takefromstr(cls,details):
        return cls(details.split("-")[0], int(details.split("-")[1]))

string = "John-1200"
e3 = EmployeeWithMethod.takefromstr(string)
print(e3.name, e3.salary)

string2 = "Johny-1000"
e4 = EmployeeWithMethod.takefromstr(string2)
print(e4.name, e4.salary)

"""
John 1200
Johny 1000
in class methods we are return cls with splitted
data so that it will create a object with that
data
"""