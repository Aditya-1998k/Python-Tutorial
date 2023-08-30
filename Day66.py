"""
Instance vs class Variable:
--------------
class Variable:
class variable defined at the class
level and are shared among all
the instance of the classes.
They are defined outside of any methods
and are usually used to store information
that is common to all instances of the
class
"""

class Employee:
    companyName = 'Zeomega Infotech'
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.2
        Employee.noOfEmployees +=1

    def showDetails(self):
        print(f"My name is {self.name} and I am working in {self.companyName} and I got appraise of {self.raise_amount} % and size of employee {self.noOfEmployees}")
        
emp1=Employee("Harry")
emp1.raise_amount= 0.3
emp1.companyName = "Apple"
emp1.showDetails()

emp2 = Employee("Aditya")
emp2.showDetails()

emp2 = Employee("Vishwa")
emp2.showDetails()

"""
Output:
My name is Harry and I am working in Apple and I got appraise of 0.3 % and size of employee 1
My name is Aditya and I am working in Zeomega Infotech and I got appraise of 0.2 % and size of employee 2
My name is Vishwa and I am working in Zeomega Infotech and I got appraise of 0.2 % and size of employee 3
--------------------
In the above example
companyName -- class variable --common for all instance (but can change at instance level
but it will not change for all)
First it will search for instance variable if not found then it will search for
same variable name in class variable
----------------
name and raise_amount--instance variable --defined inside
init method (constructor)
"""