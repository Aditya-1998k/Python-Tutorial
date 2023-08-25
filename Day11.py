"""
Strings:
anything in python inside single or 
double quote is string
"""

name = "Aditya"
friend = "Ritesh"
another_friend ='Abhinav'

"""
write below statement in print
He said, "I am a good boy"
"""

statement= 'He said, "I am a good boy"'
print(statement)

"""
We can use triple single quote or 
double quote to make multiline 
string
"""

strs= """
    this is a multiline 
    string which we can use 
    in our code based on our
    requirement
"""
print(strs)

strs= '''
    this is also a multiline string
    that we can use in our code as per 
    our requirement
'''

print(strs)

"""
Indexing in string
var ="Hello"
print(var[0])
output -->H
Indexing starts from 0
print(var[10])
output-->it will throw index error
"""
var ="python string is like an array of character"

print(var[0])
print(var[5])

"""
Looping through Strings
"""
var2="Hello World"

for char in var2:
    print(char)