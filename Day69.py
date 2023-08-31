"""
Python Class Methods:
------------
class methods are bound to the class
not instance of the class

@classmethod --decorator is used
followed by function definition

The first argument is always "cls"
which represent class itself
"""
class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and compnay is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany


emp1 = Employee()
emp1.name = "Harry"
emp1.show()
emp1.changeCompany("Tesla")
emp1.show()
print(Employee.company)

"""
The name is Harry and compnay is Apple
The name is Harry and compnay is Tesla
Tesla
----------------
by using @classmethod we can directly
change the class variable instead of
instance variable
"""