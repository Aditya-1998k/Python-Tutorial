# """Without idioms __name__"""
# def welcome():
#     print("hey welcome to the python world")

# welcome()

"""with idion __name__"""
def welcome():
    print("hey welcome to the python world")
    print(__name__)

if __name__ == "__main__":
    welcome()

"""
Output:
hey welcome to the python world
__main__

if  you will run this file directly
"""