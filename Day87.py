"""
Shutil Module in Python:
------------------
High level file operation 
Shutils is a python module that provide
higher level interface for working with file
and directories. The name 'shutil' is short
for shell utillity. It provides a convienient
and efficient way to automate task that
are commonly performed on files and directories.

shutil.copy(src, dst)--for file only
shutil.copy2(src, dst) -- for file only
shutil.copytree(src, dst) --folder
shutil.move(src, dst) --file
shutil.rmtree(path)--folder
"""

import shutil
shutil.copy("/home/ubuntu/Pictures/1.png","/home/ubuntu/Music/")
shutil.copy("/home/ubuntu/Pictures/1.png","/home/ubuntu/Music/2.png")
shutil.copy2("/home/ubuntu/Pictures/1.png","/home/ubuntu/Music/metadata.png")
"""
This function copies the file located at src to new location
specified by destination (dst). If the file already exist then
original file get overwritten.
shutil.copy2 -- this function is similar to shutil.copy but
it also preserves more metadata about the original file, such
as timestamp.
for metadat.png -- you can see details from original file also
"""

shutil.copytree("/home/ubuntu/Pictures", "/home/ubuntu/Music/NewPictures")

"""
shutil.copytree--copy the whole folder into the destination folder
here it will create a new FOlder NewPictures inside Music folder
"""

shutil.move("/home/ubuntu/Music/metadata.png", "/home/ubuntu/Pictures")
"""
This will move the file to Pictures folder from Music folder
shutil.move--move the file from source to destination
"""
import os
os.remove("/home/ubuntu/Pictures/metadata.png")

"""
No method to remove file with shutil so i used
os module
"""

shutil.rmtree("/home/ubuntu/Music/temp foder")

"""
This will delete the entire folder
shutil.rmtree --for folder only
"""