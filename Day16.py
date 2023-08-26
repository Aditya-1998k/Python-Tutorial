"""
Match Case Statements:
Just like switch statements in
C, C++ and Java
Three Entities:
    1.Match case statments
    2.cases
    3.default case

match var_name:
    case var_name_value:
        stmts
    case var_name_value:
        statements
    case _:
        default statements
"""

num = int(input("Enter the Number: "))

match num:
    case 0:
        print("Number is Zero")
    case 786:
        print("THis is special Number")
    case _:
        print("Printing by default: ",num)


"""
Writing a Program where A group of three
Friend will enter first three letters of
their name and our program will identify
them based on that
"""

name = input("Enter First three Letter of Name: ")

match name:
    case 'adi':
        print("You are Aditya")
        check = input("Am i right(yes/no)? ")
        if check =='yes':
            print("thank you")
        else:
            print("Sorry, try again!")
    case 'rit':
        print("You are Ritesh")
        check = input("Am i right(yes/no)? ")
        if check =='yes':
            print("thank you")
        else:
            print("Sorry, try again!")

    case 'tin':
        print("You are Tinku")
        check = input("Am i right(yes/no)? ")
        if check =='yes':
            print("thank you")
        else:
            print("Sorry, try again!")
    
    case _:
        print("Intruder Alert")
