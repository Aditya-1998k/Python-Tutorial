"""
File IO in Python
1.Opening a file
    f = open('myfile.txt),'r')  
    w-write
    r-read
    a-append
"""

"Reading a File"

f = open('test.py','r')
# if this file does not exist then it will throw error
# if i will use write mode if not exist it will create
# print(f)
# <_io.TextIOWrapper name='Day32.py' mode='r' encoding='UTF-8'>

text = f.read()
print(text)
# this will print all the content of the file on console
# make sure you opened the file in read mode to read the file
f.close()
# close the file after read

"Writing In file"
f = open('myfile.txt','w')
f.write("This will overide existing contents and reflect inthe myfile.txt")
f.close()
# this is very important to close the file
# after writing otherwise changes will not
# be reflected

"Appending in FIle"
f = open('myfile.txt','a')
f.write("\nTHis will appended in file without overiding the exisiting")
f.close()

"Writing in different way"
with open('myfile.txt','a') as f:
    f.write("\nHello I am New")
