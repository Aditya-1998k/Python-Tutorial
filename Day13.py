"""
String Method:
    string are immutable so we can change
    but we create new copy while applying 
    string methods
    1.upper()
    2.lower()
    3.rstrip() --can strip only trailing char
    4.replace() --replace all the occurance
    5.capitalize() --first char capitalize
            and other char to lower(imp**)
    6.center() --number of character we want to shift,
            and if we want to replace space with 
            somethin else
    7.count()--check number of occurance of char or word
    9.endswith()--checks if string ends with
      required char we can check for between 
      the index of string also
"""

name = "Hello"
print(name.upper())
print(name.lower())


name = "Hello!!!!!!"
print(name.rstrip("!"))
print(name.replace("!","?"))


name = "introduction to pyThon pyThon.py"
print(name.capitalize())
print(name.center(50,"."))
print(name.count("pyThon"))
print(name.endswith(".py"))
print(name.endswith("ti",4,10))

"""
output of above all the prints--->
HELLO
hello
Hello
Hello??????
Introduction to python python.py
.........introduction to pyThon pyThon.py.........
2
True
True
"""



"""
find(): find method seach in the string and 
return the index of first occurance
if not there then return -1

index()--this method if not found then 
return exception (only difference)

isalnum()--It will return true if all the 
characters are alphanumeric if anyother 
then return false

isalpha()-- return true if A-Z or a-z
"""
str1="He's a good boy. He is an honest Man"
print(str1.find("is"))
print(str1.find("python"))
# print(str1.index("python"))
print(str1.isalnum())
print(str1.isalpha())

"""
return 20 first case
return -1 for second case
ValueError: substring not found
False --because it is having ' apostrophe
False --because of aposhtrophe
"""

"""
islower()--if all character lower then true
        else false
isprintable()--if all the character are printable
"""

variable1="abcdefg"
variable2="AbcddD"
variable3="abcd\n"
print(variable1.islower())
print(variable2.islower())
print(variable1.isprintable())
print(variable3.isprintable())

"""
output--
True--all are lower
False--all are not lower
True--all are printable
False--\n is not printable
"""

"""
isspace()--it will return true if string
        contains white space 
        (only whitespace nothing else)
istitle()--return True only if first 
        letter of each word of the 
        string is capitalized
swapcase()--change the casing of string 
        if lower then upper case else 
        upper to lower
"""

var3=" "
var4="hello World"
print(var3.isspace())
print(var4.isspace())
print(var4.istitle())
print(var4.swapcase())

"""
True --only space
False --not only space
False --first letter not capital
HELLO wORLD --changed cases
"""

"""
title()--capitalize each letter of the
word
"""
var5 = "hello world how are you?"
print(var5.title())

"""
output-- Hello World How Are You?
"""
