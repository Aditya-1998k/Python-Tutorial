"""
Function Caching:
------------
Suppose a function is very expensive
which takes much time to execute and
we also need to execute multiple times
for same value in different part of 
our code.

import functools -- we can use this
for cache

functools.lru_cache --decorator we can use

memoization -- retrieved the data without
repeating the computation

cache value store only for single code execution
"""
import time
from functools import lru_cache

@lru_cache(maxsize=None)
def printNumber(n):
    time.sleep(5)
    return n*5

print(printNumber(10))
print("Done for 10")
print(printNumber(20))
print("Done for 20")
print(printNumber(30))
print("Done for 30")
print("Now See the Magic--No Wait cache will work for same number -memoization will work")
print(printNumber(10))
print("Done for 10")
print(printNumber(20))
print("Done for 20")
print(printNumber(30))
print("Done for 30")