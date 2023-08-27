"""
OS Module in Python:
os module in python is inbuilt 
module in python

You can perform wide variety of task
such as reading, writing files, 
interacting with file system

    1.os.mkdir()--create folder
    2.os.rename(oldfilepath, newfilepathwithnewname)
"""

import os

if not os.path.exists("data"):
    os.mkdir("data")

#if data folder will not exist it
# it will create data folder

for i in range(100):
    if not os.path.exists(f"data/Day{i+1}"):
        os.mkdir(f"data/Day{i+1}")

# it will create folder inside data folder
#100 folder inside data i.e, Day1, Day2 etc

for i in range(100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")

# it will rename all the folder from 1 to 100 with
# Day1-->Tutorial1


folders = os.listdir("data")
print(folders)

# it will list all the folder inside
# data folder
# ['Tutorial83', 'Tutorial64', 'Tutorial75',...]

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

# it will enlist all the folder and folder contained 
# by each foler

# os module have very much function 
# that we can see from documentation

print(os.getcwd())
# /home/ubuntu/Documents/python_tutorial
# it will return current working directory

os.chdir("/home/ubuntu/Documents/")
# change the directory

# os.remove() --delte file
# os.rmdir() --delete empty directory
