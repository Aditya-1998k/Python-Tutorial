"""
write a program to clear the clutter insdie a folder
on your computer. You should use os module to 
rename all the png images from 1.png all th way till
n.png where n i shte number of png files in that 
folder. Do the same for other file formates
"""

import os

fileList = os.listdir("/home/ubuntu/Pictures")
print(fileList)

for index, file in enumerate(fileList,1):
    if file.endswith(".png"):
        os.rename(f"/home/ubuntu/Pictures/{file}",f"/home/ubuntu/Pictures/{index}.png")

fileList = os.listdir("/home/ubuntu/Pictures")
print(fileList)

"""
['lobster.png', 'calculator.png']
['2.png', '1.png']

os.listdir ---gives all the file available at given paths
file.endswith--we can check if endswith (.png)
os.rename---(source, destination)
"""