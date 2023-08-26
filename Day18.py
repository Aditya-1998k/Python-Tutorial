"""
While Loop
-------------
it will execute the statement
till the condition true
---------------------
So for conditional loop we can
use while loop
"""

i=0
while(i<3):
    print(i)
    i+=1

"""
Here we initialized i at 0 and 
in our while loop condition it will
check if i <3 it will execute
and with each execution we are incrementing
the i, so till condition true it will execute
output--
0
1
2
"""


"""
Using Else Statements with While loop
when it will not go inside the loop
-------------------------------------------
The below program works till number entered
is less than or equal to 100
otherwise it will execute else statements
"""
num = int(input("Enter the Number: "))

while num<=100:
    print(i)
    num = int(input("Enter the number: "))
else:
    print("Hey You enter number greater than 100")


"""
The below program works till count >0
otherwise it will execute else statements
"""

count =5
while count>0:
    print(count)
    count-=1
else:
    print("Now Count is less than 0")


"""
Emulating Do While loop in Python:
Do while loop in other language
    do{
        loop body (execute atleast once)
    }while(condition)

"""

while True:
    num = int(input("Enter the Number: "))
    if num >=100:
        print("It's 3 digit Number, can't print")
        break
    else:
        print(num)

"""
It will execute each time if number 
is less than 100 as condition is
always true but if num is greater than 100
we have written break statement so it will 
exit of the loop
"""
