"""
Break and continue statements

break--break statements enables a
program to skip the loop and come
out of loop

continue--continue statements make
the code to skip the iteration
(us iteration ko complete kiye bina
next iteration par chale jao)
"""

for i in range(1,20):
    print("5*",i,"=",5*i)
    if i ==10:
        break
"""
it will print table of 5 upto 10 multple
Here we are using break statements which
terminate the iteration index will be 
equal to 10
"""

for i in range(21):
    if i%2==0:
        print(i)
    else:
        continue
        print("Never be Printed")

"""
The above code will print all the 
even number from 0 to 20
whenever iteration will be odd number then
we have written continue so it will go to next statement

print("Never be Printed")--This code is unreachable 
because it will never be executed as continue 
method will go directly to next statements
"""