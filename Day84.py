"""
Time module in python:
-----------
time module in python provide
a set of function to work with
time related operations.

time.time() -- return the current
time as floating point number, representing
the number of seconds since the epoch (the point
of time when the time module was initialized)
"""
import time

def usingWhile():
    index = 0
    while index < 50000:
        print(index)
        index +=1

def usingFor():
    for i in range(50000):
        print(i)

init = time.time()
usingFor()
time_taken_by_for = time.time()-init

init = time.time()
usingWhile()
time_taken_for_while = time.time()-init

print(time_taken_by_for)
print(time_taken_for_while)
print(init)

"""
output:
1.037818193435669 sec
1.744715690612793 sec
1693646020.804713 sec
The epoch is the point where the time starts, 
and is platform dependent. On Windows and 
most Unix systems, the epoch is 
January 1, 1970, 00:00:00 (UTC) and 
leap seconds are not counted towards 
the time in seconds since the epoch.
"""

"""
time.sleep()--wait for few seconds
time.sleep(4)--python will wait 5 second
to execute the next line of code
"""

print("this is printed wait for next")
time.sleep(5)
print("This is pritented after 5 seconds")


"""
time.strftime()-- 
format a time value as a string, based
on a specified time format. This function
is useful for formatting date and time
"""

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)

"""
2023-09-02 15:36:09
same format as we given in the strftime function
"""