print("hello World")

#print() function expect valid object like string, 
#integer or anyother data types
print(12*12)
print(5)


# print function expects a file-like object, not a file path as a string.
# we need to open the file in write mode, write the content to it, and then close the file

with open('/home/ubuntu/Documents/python_tutorial/pip_module.py', 'a') as f:
    print("#this is from first program", file=f)

