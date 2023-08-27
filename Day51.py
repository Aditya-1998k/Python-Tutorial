"""
seek() and tell() functions
-----------------
These function are used to work with the file
objects and their positions within a file
These functions are part of built io-module
"""

"""
seek()
seek function allows you to move the current
position within a file to a specific point.
THese position specified in bytes, and you can
move either forward or backward from the current
position
"""

with open('myfile.txt','r') as f:
    print(type(f))
    # Move to the 10th byte in the file
    f.seek(10)
    # read the next five bytes
    data = f.read(5)
    print(data)

"""
Output:
<class '_io.TextIOWrapper'>
overi
"""

"""
tell()
the tell function returns the current
position within the file in bytes. 
This can be usefult for keeping track
of your location within the file.
"""

with open("myfile.txt", "r") as f:
    f.seek(10)
    print(f.tell())

"""
Output:
10
"""

"""
truncate():
with truncate function we truncate
the file to specific size 
after that size we will not be able
to write to file
"""

with open('sample.txt', 'w') as f:
    f.write("Hellow world How are you")
    f.truncate(5)

# only first 5 character will be written 
# in the file