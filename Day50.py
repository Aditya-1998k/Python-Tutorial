"""
readline()-method reads a single line from
the file. I we want to read multiple line
we can use loop
"""

f = open("myfile.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# it will print each line one by one
#readline() only read one file at a time

"Reading Marks of students from File marks.txt"

f = open("marks.txt","r")
subjects =["Mathematics", "SocialScience", "Science"]

i = 0
while True:
    i = i+1
    line=f.readline()
    if not line:
        break
    marks=line.split(",")
    for mark in marks:
        print(f"Marks of student {i} in {subjects[i-1]} is {mark} ")

"""
Note: string.split(",")--return list
Output:
Marks of student 1 in Mathematics is 99 
Marks of student 1 in Mathematics is 56 
Marks of student 1 in Mathematics is 45
 
Marks of student 2 in SocialScience is 67 
Marks of student 2 in SocialScience is 12 
Marks of student 2 in SocialScience is 34
 
Marks of student 3 in Science is 78 
Marks of student 3 in Science is 98 
Marks of student 3 in Science is 99 
"""

"""
writelines()--
this methods will write a sequence of string 
to the file
The sequence can be any iterable objects
like list, tuples etc
it will not write new line characters at the 
end of the line
"""
contents = ["\nHello world\n", "How are you\n","I am Aditya\n"]

f = open("myfile.txt",'a')
f.writelines(contents)
f.close()

