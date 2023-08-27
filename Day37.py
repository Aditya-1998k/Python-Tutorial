"""
finally clause in python:
------------------------
that is very useful when we deal
with function with try except

finally always executed if after 
function return
"""

def func():
    try:
        arr = [1,2,3,4,5,6,7]
        i = int(input("ENter the index: "))
        print(arr[i])
        return 1
    except:
        print("Invalid Index")
        return 0
    finally:
        print("I am always executed")

print(func())

"""
ENter the index: 123
Invalid Index
I am always executed --after finally block returns happens
0
------------------------------
finally block execute hone ke baad
hi function return karega
"""

def func():
    try:
        arr = [1,2,3,4,5,6,7]
        i = int(input("ENter the index: "))
        print(arr[i])
        return 1
    except:
        print("Invalid Index")
        return 0
    
    print("I will never be executed")

print(func())

"""
ENter the index: 12
Invalid Index
0
"""
